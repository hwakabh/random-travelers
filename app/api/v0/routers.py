from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from app.api.v0 import schemas

router = APIRouter()


@router.get('/')
def index(req: Request) -> schemas.RootResponse:

    return JSONResponse(content={
        "path": req.url.path,
        "detail": "v0 API has been deprecated, please access v1 API with /api/v1/"
    })
