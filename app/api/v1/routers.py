import requests
import os

from fastapi import APIRouter, Response

from .cruds import get_country


router = APIRouter()

@router.get('/')
def index():
    return {
        "path": "v1 API root, /api/v1/"
    }


@router.post('/shuffle')
def get_random_country():
    result = get_country()
    return result


@router.get('/fetch')
def fetch_google_api_key():

    resp = ""
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', None)
    if GOOGLE_MAPS_API_KEY is None:
        # TODO: Implement with raise error for client-side
        print("Failed to load API KEY")
        pass

    url = f'https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API_KEY}'
    resp = requests.get(url).text

    return Response(
        content=resp,
        headers={"Content-Type": "text/javascript"},
    )
