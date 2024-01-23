from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from sqlalchemy.orm import Session

from app.api.v1 import services
from app.api.v1 import cruds
from app.api.v1 import schemas
from app.api.v1 import models
from app.database import get_db, engine

router = APIRouter()
# Create table if not exists on application startup
models.Base.metadata.create_all(bind=engine)


@router.get('/')
def index(req: Request) -> schemas.RootResponse:
    return JSONResponse(content={
        "path": req.url.path,
        "detail": "v1 API root"
    })


@router.get('/fetch')
def fetch() -> Response:
    return services.load_google_map()


@router.post('/shuffle')
def get_random_country(
    payload: schemas.SearchRequestBody,
    db: Session = Depends(get_db)
) -> schemas.SearchResultResponseBody:

    country = services.get_random_country()
    print(f'Randomly selected country: {country}')

    return cruds.get_destination(db=db, req=payload)


@router.post('/translate')
def translate(req: schemas.TranslateReqBody) -> str:
    # Filter only country name to translate
    country_name = req.model_dump().get('country')
    return services.translate_county_name(txt=country_name)
