import json
import random
from math import sin, cos, acos, radians

import mysql.connector as mydb
import numpy as np
import requests
from sqlalchemy.orm import Session

from app.api.v1 import models
from app.api.v1 import schemas
from app.config import app_settings


# TODO: should be used with ORM
conn = mydb.connect(
    host=app_settings.MYSQL_HOST,
    user=app_settings.MYSQL_USER,
    password=app_settings.MYSQL_PASSWORD,
    database=app_settings.MYSQL_DATABASE,
    charset="utf8"
)


def get_airports_from_db(db: Session) -> schemas.Airport:
    return db.query(models.Airport).limit(5).all()


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


# --- search and get near airport from MySQL (airport table)
def get_near_airport(current_lat,current_lng):

    conn.ping(reconnect=True)
    cur = conn.cursor()

    print("gacha.py get values - current_lat: " + current_lat)
    print("gacha.py get values - current_lng: " + current_lng)

    current = float(current_lat), float(current_lng)
    target = []
    dist_result = []
    search_key = []
    count = 0

    cur.execute('select id,IATA,Name,Country,City,Latitude,Longitude from airport where not IATA="NULL"')

    for sql_result in cur.fetchall():
        target = sql_result[5], sql_result[6]
        dist = dist_on_sphere(current, target)
        dist_result.append([count,sql_result[0],sql_result[1],sql_result[2],sql_result[3],sql_result[4],dist])
        search_key.append(dist)
        count = count + 1

    cur.close()
    conn.close()

    #print(dist_result)
    #print(search_key)

    #--- return near airport IATA
    return dist_result[np.argmin(search_key)][2]


#--- search and get reachable location (airport and country) from skyscanner api
#--- exclude if time and travel expenses exceed the user input parameter
#--- select a country at random
def get_destination_from_skyscanner_by_random(near_airport_IATA,time_limit,expense_limit):

    print("gacha.py get values - near_airport_IATA: " + near_airport_IATA)
    print("gacha.py get values - time_limit: " + time_limit)
    print("gacha.py get values - expense_limit: " + expense_limit)

    # --- search and get reachable location (airport and country) from skyscanner api
    # --- exclude if time and travel expenses exceed the user input parameter

    ##########################################################################################
    ##################################### Update required #####################################
    ###########################################################################################

    #reachable_airport_IATA = ["TXL","YTD","CQS","NYR","QFG","NZE","IWK"]

    conn.ping(reconnect=True)
    cur = conn.cursor()

    cur.execute('select IATA from airport where not IATA="NULL"')
    reachable_airport_IATA = []
    for sql_result in cur.fetchall():
        reachable_airport_IATA.append(sql_result[0])

    cur.close()
    conn.close()

    ##########################################################################################
    ##########################################################################################
    ##########################################################################################

    #--- select a country at random
    random_airport_IATA = random.choice(reachable_airport_IATA)

    #--- get lat/lng of near and selected airport from MySQL (airport table)
    conn.ping(reconnect=True)
    cur = conn.cursor()

    cur.execute('select Country,City,IATA,Name,Latitude,Longitude from airport where IATA="' + near_airport_IATA + '"')
    transit = []
    for sql_result in cur.fetchall():
        transit.append([sql_result[0],sql_result[1],sql_result[2],sql_result[3],sql_result[4],sql_result[5]])

    cur.execute('select Country,City,IATA,Name,Latitude,Longitude from airport where IATA="' + random_airport_IATA + '"')
    destination = []
    for sql_result in cur.fetchall():
        destination.append([sql_result[0],sql_result[1],sql_result[2],sql_result[3],sql_result[4],sql_result[5]])

    cur.close()
    conn.close()

    return json.dumps({
        "tran_country":transit[0][0],
        "tran_city":transit[0][1],
        "tran_iata":transit[0][2],
        "tran_airport":transit[0][3],
        "tran_lat":transit[0][4],
        "tran_lng":transit[0][5],
        "dest_country":destination[0][0],
        "dest_city":destination[0][1],
        "dest_iata":destination[0][2],
        "dest_airport":destination[0][3],
        "dest_lat":destination[0][4],
        "dest_lng":destination[0][5]
    })


#--- Distance calculation between two points
earth_rad = 6378.137

def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

def dist_on_sphere(pos0, pos1, radius=earth_rad):
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radius
