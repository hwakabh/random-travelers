from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request


router = APIRouter()


@router.get('/')
def index(req: Request) -> JSONResponse:

    return JSONResponse(content={
        "path": req.url.path,
        "detail": "v0 API has been deprecated, please access v1 API with /api/v1/"
    })
