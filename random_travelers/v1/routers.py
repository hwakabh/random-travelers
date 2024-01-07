from fastapi import APIRouter

from .cruds import get_country


router = APIRouter()

@router.get('/')
def index():
    return '/api/v1/ root URL'
    # TODO: replace render_template for FastAPI
    # return render_template('index_v01.html')


@router.get('/gacha_v01')
def gacha_ver01_result():
    result = get_country()
    return result
