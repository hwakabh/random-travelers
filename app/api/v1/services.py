import json
import random

from fastapi.responses import Response
import httpx

from app.config import app_settings


def load_google_map() -> Response:

    API_KEY = app_settings.GOOGLE_MAPS_API_KEY
    if API_KEY == '':
        print("Failed to load API KEY, will use raw response from API")
        return ""

    url = f'https://maps.googleapis.com/maps/api/js?key={API_KEY}'
    resp = httpx.get(url).text

    return Response(
        content=resp,
        headers={"Content-Type": "text/javascript"},
    )


def translate_county_name(txt: str) -> str:

    API_KEY = app_settings.GOOGLE_MAPS_API_KEY
    if API_KEY == '':
        print("Failed to load API KEY, will use raw response from API")
        return ""

    url = f'https://translation.googleapis.com/language/translate/v2?key={API_KEY}&q={txt}&source=en&target=ja'

    # Spoofing referer for Cloud Translate API
    resp = httpx.post(url, headers={"Referer": "http://localhost:3000/"}).json()
    if resp.get('error'):
        print('Failed to fetch result from Translate API, returning bare response of API for UI.')
        return ""

    return resp.get('data').get('translations')[0].get('translatedText')
