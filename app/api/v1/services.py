import json
import random

from fastapi.responses import Response
import httpx

from app.config import app_settings
from app.api.v1.schemas import TranslateReqBody


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


def translate_county_name(txt: TranslateReqBody) -> str:

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

    # Select region randomly
    region = []
    for x in range(0,len(data)):
        if data[x]['region'] != '':
            region.append(data[x]['region'])

    region_result = random.choice(list(set(region)))

    # Select country randomly
    country = []
    for x in range(0,len(data)):
        if data[x]['region'] == region_result:
            country.append(data[x]['name']['official'])

    country_result = random.choice(country)

    return country_result
