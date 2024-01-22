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


@router.get('/search')
def get_flight_search_result():
    #--- get ajax POST data
    time_limit = requests.json["time_limit"]
    expense_limit = requests.json["expense_limit"]
    current_lat = requests.json["current_lat"]
    current_lng = requests.json["current_lng"]
    print("main.py ajax POST data - time_limit: " + time_limit)
    print("main.py ajax POST data - expense_limit: " + expense_limit)
    print("main.py ajax POST data - current_lat: " + current_lat)
    print("main.py ajax POST data - current_lng: " + current_lng)

    #--- search and get near airport from MySQL (airport table)
    near_airport_IATA = get_near_airport(current_lat,current_lng)
    print("main.py get values - near_airport_IATA: " + near_airport_IATA)

    #--- search and get reachable location (airport and country) from skyscanner api
    #--- exclude if time and travel expenses exceed the user input parameter
    #--- select a country at random
    destination = get_destination_from_skyscanner_by_random(near_airport_IATA,time_limit,expense_limit)
    return destination


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
