from fastapi import APIRouter, requests

from .cruds import get_destination_from_skyscanner_by_random, get_near_airport


router = APIRouter()

@router.get('/')
def index():
    return '/api/v0/ root URL'
    # TODO: replace render_template for FastAPI
    # return render_template('index.html')


@router.get('/gacha')
def gacha_result():
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

