from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get('/')
def index() -> JSONResponse:
    return JSONResponse(content={
        "path": "/api/v0/",
        "detail": "v0 API has been deprectiated, please access v1 API with /api/v1/"
    })
