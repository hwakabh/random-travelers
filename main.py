# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import gacha
import gacha_v01 ### version01
import json

app = Flask(__name__)


#---------------------------------
# latest
#---------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gacha', methods=['GET', 'POST'])
def gacha_result():

    #--- get ajax POST data
    time_limit = request.json["time_limit"]
    expense_limit = request.json["expense_limit"]
    current_lat = request.json["current_lat"]
    current_lng = request.json["current_lng"]
    print("main.py ajax POST data - time_limit: " + time_limit)
    print("main.py ajax POST data - expense_limit: " + expense_limit)
    print("main.py ajax POST data - current_lat: " + current_lat)
    print("main.py ajax POST data - current_lng: " + current_lng)

    #--- search and get near airport from MySQL (airport table)
    near_airport_IATA = gacha.get_near_airport(current_lat,current_lng)
    print("main.py get values - near_airport_IATA: " + near_airport_IATA)

    #--- search and get reachable location (airport and country) from skyscanner api
    #--- exclude if time and travel expenses exceed the user input parameter
    #--- select a country at random
    destination = gacha.get_destination_from_skyscanner_by_random(near_airport_IATA,time_limit,expense_limit)
    return destination


#---------------------------------
# version01
#---------------------------------
@app.route('/v01')
def ver01():
    return render_template('index_v01.html')

@app.route('/gacha_v01', methods=['GET', 'POST'])
def gacha_ver01_result():
    result = gacha_v01.get_country()
    return result


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
