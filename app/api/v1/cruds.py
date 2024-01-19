import json
import random

import requests

def get_country():
    # import data
    try:
        url = 'https://restcountries.com/v3.1/all?fields=region,name'
        data = requests.get(url).json()

    except requests.exceptions.HTTPError as e:
        print('HTTPError: ', e)

    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    # Select region randomly
    region = []
    for x in range(0,len(data)):
        if data[x]['region'] != '':
            region.append(data[x]['region'])

    region_result = random.choice(list(set(region)))
    print(f"Region selected: {region_result}")

    # Select country randomly
    country = []
    for x in range(0,len(data)):
        if data[x]['region'] == region_result:
            country.append(data[x]['name']['official'])

    country_result = random.choice(country)
    print(f"Country selected: {country_result}")

    return country_result

