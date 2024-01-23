import json
import random

from fastapi.responses import Response
import httpx

from app.config import app_settings


def load_google_map() -> Response:

    API_KEY = app_settings.GOOGLE_MAPS_API_KEY
    if API_KEY is None:
        # TODO: Implement with raise error for client-side
        print("Failed to load API KEY")
        pass

    url = f'https://maps.googleapis.com/maps/api/js?key={API_KEY}'
    resp = httpx.get(url).text

    return Response(
        content=resp,
        headers={"Content-Type": "text/javascript"},
    )


def translate_county_name(txt: str) -> str:

    API_KEY = app_settings.GOOGLE_MAPS_API_KEY
    if API_KEY is None:
        # TODO: Implement with raise error for client-side
        print("Failed to load API KEY")
        pass

    url = f'https://translation.googleapis.com/language/translate/v2?key={API_KEY}&q={txt}&source=en&target=ja'

    # Spoofing referer for Cloud Translate API
    resp = httpx.post(url, headers={"Referer": "http://localhost:3000/"}).json()

    return resp.get('data').get('translations')[0].get('translatedText')


def get_random_country() -> str:
    try:
        url = 'https://restcountries.com/v3.1/all?fields=region,name'
        data = httpx.get(url).json()

    except httpx.HTTPError as e:
        print('HTTPError: ', e)

    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    # Fetch regions list with removing duplication
    regions = sorted(set([country.get('region') for country in data]))
    region = random.choice(regions)

    # Select country randomly
    countries = [c.get('name').get('official') for c in data if c.get('region') == region]

    return random.choice(countries)
