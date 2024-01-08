from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from mako.template import Template

from .cruds import get_country


router = APIRouter()

@router.get('/', response_class=HTMLResponse)
def index():
    tmpl = Template(filename='templates/index_v01.html')
    return tmpl.render(ctx='This is v1 templates')


@router.get('/gacha_v01')
def gacha_ver01_result():
    result = get_country()
    return result
