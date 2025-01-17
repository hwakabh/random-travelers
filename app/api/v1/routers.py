from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from sqlalchemy.orm import Session, sessionmaker

from app.api.v1 import services
from app.api.v1 import cruds
from app.api.v1 import schemas
from app.api.v1 import models
from app.api.v1.helpers import convert_csv_to_list
from app.database import get_db, engine

router = APIRouter()
# Create table if not exists on application startup
models.Base.metadata.create_all(bind=engine)
# Load fixture data (TODO: add precheck logics for avoiding duplication error)
try:
    # TODO: make DRY with database.py
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    # TODO: make dynamic (refs: #128)
    filename = 'sql/airport.csv'
    data: list = convert_csv_to_list(f=filename)
    print(f'loading data from {filename} ...')
    for i in data:
        record = models.Airport(**{
            'id' : i[0],
            'name': i[1],
            'city': i[2],
            'country': i[3],
            'IATA': i[4].replace('\"', ''),
            'ICAO': i[5].replace('\"', ''),
            'latitude': i[6],
            'longitude': i[7],
            'altitude': i[8],
            'tz_offset': i[9],
            'DST': i[10].replace('\"', ''),
            'tz_dbtime': i[11],
            'types': i[12],
            'datasource': i[13],
        })
        s.add(record)
    s.commit()
    print(f'loaded {len(data)} lines')
except Exception as e:
    s.rollback()
    print(e)
finally:
    s.close()


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
def translate(req: schemas.TranslateReqBody) -> schemas.TranslateRespBody:
    # Filter only country name to translate
    country_name = req.model_dump().get('country')

    return schemas.TranslateRespBody(
        translated=services.translate_county_name(txt=country_name)
    )
