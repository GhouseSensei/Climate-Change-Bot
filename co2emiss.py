from geopy.geocoders import Nominatim
import geopy.distance

def chicken(val):
    val = int(val)
    return [val*3.7/1000, val*0.5/1000, val*2/1000]

def mutton(val):
    val = int(val)
    return [val*27/1000, val*0.5/1000, val*2/1000]

def beef(val):
    val = int(val)
    return [val*23/1000, val*0.5/1000, val*2/1000]

def pork(val):
    val = int(val)
    return [val*6/1000, val*0.5/1000, val*2/1000]

def lpg(val):
    val = int(val)
    return val*3.988

def petrol(val):
    val = int(val)
    return val*0.3

def diesel(val):
    val = int(val)
    return val*0.25

def bike(val):
    val = int(val)
    return val*0.2

def flight(s1, s2):
    geolocator = Nominatim(user_agent="MyApp")
    location1 = geolocator.geocode(s1)
    location2 = geolocator.geocode(s2)
    pt1 = [location1.latitude, location1.longitude]
    pt2 = [location2.latitude, location2.longitude]
    if(geopy.distance.geodesic(pt1, pt2).km<400):
        return [0, 500]
    elif(geopy.distance.geodesic(pt1, pt2).km>= 400 and geopy.distance.geodesic(pt1, pt2).km<1200):
        return [500, 900]
    elif(geopy.distance.geodesic(pt1, pt2).km>= 1200 and geopy.distance.geodesic(pt1, pt2).km<2400):
        return [1000, 1700]
    elif(geopy.distance.geodesic(pt1, pt2).km>= 2400 and geopy.distance.geodesic(pt1, pt2).km<4800):
        return [1700, 2500]
    elif(geopy.distance.geodesic(pt1, pt2).km>= 4800 and geopy.distance.geodesic(pt1, pt2).km<8800):
        return [2500, 5500]
    else:
        return[7000]
