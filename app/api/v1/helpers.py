from math import sin, cos, acos, radians


# Helper functions for cruds.py
#--- Distance calculation between two points
EARTH_RAD = 6378.137

def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat * cos(rlng), coslat * sin(rlng), sin(rlat)


def dist_on_sphere(pos0, pos1, radius=EARTH_RAD):
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radius


# Helper functions for services.py
