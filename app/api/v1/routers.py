from fastapi import APIRouter

from .cruds import get_country


router = APIRouter()

@router.get('/')
def index():
    return {"path": "v1 API root, /api/v1/"}


@router.post('/shuffle')
def get_random_country():
    result = get_country()
    return result
