from math import sin, cos, acos, radians
import csv

import httpx

# Helper functions for cruds.py
#--- Distance calculation between two points
EARTH_RAD = 6378.137

def latlng_to_xyz(lat: float, lng: float) -> float:

    rlat = radians(lat)
    rlng = radians(lng)
    coslat = cos(rlat)

    return coslat * cos(rlng), coslat * sin(rlng), sin(rlat)


def dist_on_sphere(
        pos0: tuple,
        pos1: tuple,
        radius: float = EARTH_RAD
) -> float:

    src_xyz = latlng_to_xyz(*pos0)
    dst_xyz = latlng_to_xyz(*pos1)

    return acos(sum(x * y for x, y in zip(src_xyz, dst_xyz))) * radius


# Helper functions for services.py

# Helper functions for database.py
def fetch_airport_data() -> list:
    # Raw data of https://github.com/jpatokal/openflights/blob/master/data/airports.dat
    url = "https://raw.githubusercontent.com/jpatokal/openflights/refs/heads/master/data/airports.dat"
    try:
        dat = httpx.get(url).text
    except:
        return []

    return [ r for r in csv.reader(dat.strip().splitlines()) ]
