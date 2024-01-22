import requests
import os

from fastapi import APIRouter, Response, Depends
from sqlalchemy.orm import Session

from app.api.v1.cruds import get_country, get_airports_from_db
from app.api.v1.schemas import TranslateReqBody, Airport
from app.config import app_settings
from app.database import get_db

router = APIRouter()


@router.get('/')
def index() -> dict:
    return {
        "path": "v1 API root, /api/v1/"
    }


@router.get('/airports')
def get_airports(db: Session = Depends(get_db)) -> list[Airport]:
    return get_airports_from_db(db=db)


@router.post('/shuffle')
def get_random_country():
    result = get_country()
    return result


@router.get('/fetch')
def fetch_google_api_key() -> Response:

    API_KEY = app_settings.GOOGLE_MAPS_API_KEY
    if API_KEY is None:
        # TODO: Implement with raise error for client-side
        print("Failed to load API KEY")
        pass

    url = f'https://maps.googleapis.com/maps/api/js?key={API_KEY}'
    resp = requests.get(url).text

    return Response(
        content=resp,
        headers={"Content-Type": "text/javascript"},
    )


@router.post('/translate')
def translate(req: TranslateReqBody) -> str:

    API_KEY = app_settings.GOOGLE_MAPS_API_KEY
    if API_KEY is None:
        # TODO: Implement with raise error for client-side
        print("Failed to load API KEY")
        pass

    text = req.model_dump().get('country')
    url = f'https://translation.googleapis.com/language/translate/v2?key={API_KEY}&q={text}&source=en&target=ja'

    # Spoofing referer for Cloud Translate API
    resp = requests.post(url, headers={"Referer": "http://localhost:3000/"}).json()

    return resp.get('data').get('translations')[0].get('translatedText')
