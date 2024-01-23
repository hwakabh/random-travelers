import random

import numpy as np
from sqlalchemy.orm import Session

from app.api.v1 import models
from app.api.v1 import schemas
from app.api.v1.helpers import dist_on_sphere


# Bind cruds functions for return results to router
def get_destination(db: Session, req: schemas.SearchRequestBody):
    #--- get ajax POST data
    print(f'User conditions: {req}')

    #--- search and get near airport from MySQL (airport table)
    near_airport_IATA = get_near_airport(
        db=db,
        lat=req.current_lat,
        lng=req.current_lng
    )
    print("near_airport_IATA: " + near_airport_IATA)

    #--- search and get reachable location (airport and country) from skyscanner api
    #--- exclude if time and travel expenses exceed the user input parameter
    #--- select a country at random
    destination = get_destination_from_skyscanner_by_random(
        db=db,
        iata=near_airport_IATA
    )
    print('Destination: ')
    print(destination)

    return schemas.SearchResultResponseBody(**destination)


# --- search and get near airport from MySQL (airport table)
def get_near_airport(db: Session, lat: float, lng: float) -> str:
    target = []
    dist_result = []
    search_key = []
    count = 0

    airports = db.query(
        models.Airport.id,
        models.Airport.IATA,
        models.Airport.name,
        models.Airport.country,
        models.Airport.city,
        models.Airport.latitude,
        models.Airport.longitude
    ).filter(
        models.Airport.IATA != "NULL"
    ).all()

    for airport in airports:
        target = airport[5], airport[6]
        dist = dist_on_sphere(
            pos0=(lat, lng),
            pos1=target
        )
        dist_result.append([count,airport[0],airport[1],airport[2],airport[3],airport[4],dist])
        search_key.append(dist)
        count = count + 1

    #--- return near airport IATA
    return dist_result[np.argmin(search_key)][2]


#--- search and get reachable location (airport and country) from skyscanner api
#--- exclude if time and travel expenses exceed the user input parameter
#--- select a country at random
def get_destination_from_skyscanner_by_random(db: Session, iata: str) -> dict:
    # --- search and get reachable location (airport and country) from skyscanner api
    # --- exclude if time and travel expenses exceed the user input parameter

    airport_codes = db.query(models.Airport.IATA).filter(models.Airport.IATA != "NULL").all()

    reachable_airport_IATA = [airport_code[0] for airport_code in airport_codes]
    #--- select a country at random
    random_airport_IATA = random.choice(reachable_airport_IATA)

    #--- get lat/lng of near and selected airport from MySQL (airport table)
    transit_airports = db.query(
        models.Airport.country,
        models.Airport.city,
        models.Airport.IATA,
        models.Airport.name,
        models.Airport.latitude,
        models.Airport.longitude,
    ).filter(
        models.Airport.IATA == iata
    ).all()

    transit = []
    for airport in transit_airports:
        transit.append([airport[0],airport[1],airport[2],airport[3],airport[4],airport[5]])

    destination_airports = db.query(
        models.Airport.country,
        models.Airport.city,
        models.Airport.IATA,
        models.Airport.name,
        models.Airport.latitude,
        models.Airport.longitude,
    ).filter(
        models.Airport.IATA == random_airport_IATA
    ).all()

    destination = []
    for airport in destination_airports:
        destination.append([airport[0],airport[1],airport[2],airport[3],airport[4],airport[5]])

    return {
        "tran_country": transit[0][0],
        "tran_city": transit[0][1],
        "tran_iata": transit[0][2],
        "tran_airport": transit[0][3],
        "tran_lat": transit[0][4],
        "tran_lng": transit[0][5],
        "dest_country": destination[0][0],
        "dest_city": destination[0][1],
        "dest_iata": destination[0][2],
        "dest_airport": destination[0][3],
        "dest_lat": destination[0][4],
        "dest_lng": destination[0][5]
    }
