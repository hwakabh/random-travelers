# coding: utf-8

import json
import urllib.request
import random
import codecs
import subprocess


# import data
try:
    url = 'https://restcountries.eu/rest/v2/all?fields=region;name'
    res = urllib.request.urlopen(url)
    data = json.loads(res.read().decode('utf-8'))

    # for x in data:
        # print(x, file=codecs.open('output.txt', 'a', 'utf-8'))

except urllib.error.HTTPError as e:
    print('HTTPError: ', e)
except json.JSONDecodeError as e:
    print('JSONDecodeError: ', e)


# Select region randomly
def region():
    region = []
    region_list = []

    for x in range(0,len(data)):
        if data[x]['region'] != '':
            region.append(data[x]['region'])

    region_result = random.choice(list(set(region)))
    print(region_result)
    country(region_result)


# Select country randomly
def country(val):
    country = []

    for x in range(0,len(data)):
        if data[x]['region'] == val:
            country.append(data[x]['name'])

    country_result = random.choice(country)
    print(country_result)

    # print(subprocess.check_output("cat /home/centos/random-travelers/output.txt | grep \"" + country_result + "\"", shell=True))
    # print(subprocess.check_output("rm /home/centos/random-travelers/output.txt", shell=True))

region()

