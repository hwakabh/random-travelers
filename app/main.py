from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from mako.template import Template

from .api.v0.routers import router as router_v0
from .api.v1.routers import router as router_v1

app = FastAPI(
    title='random-travelers',
    description='API to communicate with backend database',
)

app.mount(path='/static', app=StaticFiles(directory='./app/static'), name='static')

@app.get('/', response_class=HTMLResponse)
def root():
    tmpl = Template(filename='./app/templates/index.html.mako')

    ctx = {
      "time": [6, 12, 18, 24],
      "amount": [1000, 2000, 3000, 4000, 5000]
    }

    return tmpl.render(ctx=ctx)


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

