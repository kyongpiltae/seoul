
"""
distEarth : compute distance between
2 location using latitude & longitude

-> using math library

radian(d)
    convert degree to radian

dist_between_loc(loc1, loc2)
    compute distance between 2 locations

loc_dist()
    interface that interacts with user
"""
import math


# convert degree to radian
def radian(d):
    """
    :param d: degree
    :return: radian that converted from degree
    """
    return math.radians(d)


# distance between loc1 & loc2
# using latitude & longitude
def dist_between_loc(loc1, loc2):
    """
    :param loc1: (latitude, longitude)
    :param loc2: (latitude, longitude)
        -> tuple that contains latitude at index 0,
                               longitude at index 1
    :return: distance between 2 location
    """
    # earth's radius
    r = 6371000  # meter

    '''
    𝒄𝒐𝒔 𝜽 = 𝒔𝒊𝒏(𝒍𝒂𝒕𝟏) 𝒔𝒊𝒏(𝒍𝒂𝒕𝟐) + 𝒄𝒐𝒔(𝒍𝒂𝒕𝟏) 𝒄𝒐𝒔(𝒍𝒂𝒕𝟐) 𝒄𝒐𝒔(𝒍𝒐𝒏𝟐 − 𝒍𝒐𝒏𝟏)
    𝜽 = 𝒂𝒄𝒐𝒔(𝒄𝒐𝒔 𝜽 )

    '''

    
    
    # convert latitudes of loc1 and loc2 to radian
    lat1 = radian(loc1[0])
    lon1 = radian(loc1[1])
    lat2 = radian(loc2[0])
    lon2 = radian(loc2[1])

    temp = loc2[1]- loc1[1]
    # convert difference of longitudes to radian
    #   : compute difference in degree form

    # cos(theta) : theta - radian of two location

    # get theta by acos
    theta = math.sin(lat1) * math.sin(lat2) + math.cos(lat1)* math.cos(lat2)* math.cos(radian(temp))

    # radius * theta = distance (r * 2pi = circumference of circle)
    theta=math.acos(theta)
    return r * theta


# interact with user
def loc_dist():
    """
    get two location (pair of latitude & longitude)
        loc := tuple contains lat & lon
    print distance between 2 locations
    :return: None
    """
    # call input() function without parameter
    # get first loc's latitude & longitude

    
    p1 = input("enter first  latitude and longitude ")
    p2 = input("enter first  latitude and longitude ")
    
    # store at tuple
    '''
    p1="20 40"
    p2="60 80"
    '''    
     
    l1 = p1.split()
    loc1 = (float(l1[0]), float(l1[1]))
    l2 = p2.split()
    loc2 = (float(l2[0]), float(l2[1]))

    # get second loc's latitude & longitude

    # store at tuple
   
    # print distance between 2 locations
    print(dist_between_loc(loc1, loc2))


if __name__ == '__main__':
    loc_dist()
