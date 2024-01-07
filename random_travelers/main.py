from fastapi import FastAPI

from .v0.routers import router as router_v0
from .v1.routers import router as router_v1

app = FastAPI(
    title="random-travelers",
    description="API to communicate with backend database",
)


@app.get('/')
def root():
    return {}


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

