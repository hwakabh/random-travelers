from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from mako.template import Template

from app.api.v0.routers import router as router_v0
from app.api.v1.routers import router as router_v1
from app.api.v1 import models
from app.database import engine, insert_fixtures


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create table if not exists on application startup
    models.Base.metadata.create_all(bind=engine)
    # Load fixture data (TODO: add precheck logics for avoiding duplication error)
    filename = 'sql/airport.csv'
    is_initialized = insert_fixtures(filename=filename)
    if not is_initialized:
        print('Failed to insert fixture data ...')

    yield

    try:
        print("Shutting down the applications ...")
    except Exception as e:
        pinrt(e)


app = FastAPI(
    title='random-travelers',
    description='API to communicate with backend database',
    lifespan=lifespan
)

app.mount(
    path='/static',
    app=StaticFiles(directory='./app/static'),
    name='static'
)


@app.get('/', response_class=HTMLResponse)
def root():
    tmpl = Template(filename='./app/templates/index.html.mako')

    context = {
      "time": [6, 12, 18, 24],
      "amount": [1000, 2000, 3000, 4000, 5000]
    }

    return tmpl.render(ctx=context)


@app.get('/healthz')
def healthz():
    return {"status": "ok"}


app.include_router(
    router_v0,
    prefix='/api/v0',
    tags=['API v0'],
)


app.include_router(
    router_v1,
    prefix='/api/v1',
    tags=['API v1'],
)
