
"""
Python Basic Lab 2-0
Compute distance between
2 cities using latitude & longitude

get_cities()
    making dict {key:= name : val:= loc}
        loc:= (lat, lon) <- tuple

get_city_by_name(cities, name)
    get loc from cities <- using DB from get_cities

city_dist()
    interact with user
"""
import math
from distEarth import dist_between_loc

"""
just copy & paste 2 functions 
from distEarth.py
- radian(d
- dist_between_loc(loc1, loc2)
"""

'''
# convert degree to radian
def radian(d):
    """
    just copy and paste from distEarth.py
    """
    pass # remove this


# distance between loc1 & loc2
# using latitude & longitude

def dist_between_loc(loc1, loc2):
    """
    just copy and paste from distEarth.py
    """
    pass # remove this

'''
# from 'cities.txt' get
# name of city                  <- str      : key
# (latitide, longitude) loc     <- tuple    : val
# => make cities                <- dict
def get_cities():
    """
    :return: cities <- dict {key:= name : val:= loc}
                    loc:= (lat, lon) <- tuple
    """
    # try to open file : 'cities.txt'

    try:
        fh = open('cities.txt')
    except:
        print("open error")
        exit(0)
    
    cities = dict()
    for line in fh:
        words = line.split('\t')
        name = words[0].split(",")[0]
    
        cities[name] = ( float(words[1]) , float(words[2])  )

 

    # read info from file line by line
        # split the line

        # get city name without country name

        # get latitude & longitude

        # store info in names & locs

    # return names & locs
    return cities


# get location (lat, lon) by name
def get_city_by_name(cities, name):
    """
    :param cities: dict {key:= name : val:= loc}
    :param name: name of city to find
    :return: loc <- (latitude, longitude) : tuple
    """
    # check name is in cities
    # if there are no such name, return None

    return cities.get(name,None)


# interface
def city_dist():
    """
    :return: None
    """
    # call 'the get_cities' to get a DB

    # while user enter 'EXITprogram' processing
        # call input() with out parameter
        # be careful '\n' : using strip()

        # if 'EXITprogram' stop the program

        # get two locs using 'get_city_by_name'
        # CAUTION : two city names separated by ', '

        # if loc1 and loc2 in cities's name print dist
        # else print 'There are no ~' (~ : wrong name)

    # exit the program
    # CAUTION : if user enter 'EXITprogram', then print 'exit'

    cities=get_cities()

    while(True):
        data=input()
        if(data == 'EXITprogram'):
            break
        
        citylist =data.split(",")
        city1 = citylist[0].strip()
        city2 = citylist[1].strip()
        loc1=get_city_by_name(cities,city1)
        loc2=get_city_by_name(cities,city2)
        if( loc1 is None ):
            print("theres is no ", city1)
            continue
        if( loc2 is None ):
            print("theres is no ", city2)
            continue
        print(dist_between_loc(loc1, loc2))
    print("Exit")
    exit(0)


if __name__ == '__main__':
    city_dist()
