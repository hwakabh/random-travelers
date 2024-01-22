from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
# from sqlalchemy.orm import Session

from app.api.v1 import services
from app.api.v1 import cruds
from app.api.v1 import schemas
from app.database import get_db

router = APIRouter()


@router.get('/')
def index(req: Request) -> schemas.RootResponse:
    return JSONResponse(content={
        "path": req.url.path,
        "detail": "v1 API root"
    })


# @router.get('/airports')
# def get_airports(db: Session = Depends(get_db)) -> list[schemas.Airport]:
#     return cruds.get_airports_from_db(db=db)


@router.get('/fetch')
def fetch() -> Response:
    return services.load_google_map()


@router.post('/shuffle')
def get_random_country(payload: schemas.SearchRequestBody):
    country = services.get_random_country()
    print(f'Randomly selected country: {country}')

    return cruds.get_destination(req=payload)


@router.post('/translate')
def translate(req: schemas.TranslateReqBody) -> str:
    # Filter only country name to translate
    country_name = req.model_dump().get('country')
    return services.translate_county_name(txt=country_name)
