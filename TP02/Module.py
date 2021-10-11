import math

def EquiRectDist(la1, lo1, la2, lo2):
    """
    Compute distance between 2 points with Equirectangular approximation
    this approximation is appropriate for small distances
    longitude and latitude are supposed to be in radian
    """
    R = 6371*(10**3)
    x = (lo2-lo1) * math.cos((la1+la2)/2)
    y = la2 - la1
    d = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) * R
    return d


def SommeDistance(trajet):
    sommed = 0
    for l in range(len(trajet)-1):
        sommed += EquiRectDist(math.radians(trajet[l][0]), math.radians(trajet[l][1]), math.radians(trajet[l+1][0]), math.radians(trajet[l+1][1]))

    return sommed


def SommeDuree(trajet):
    sommet = (trajet[-1][4]-trajet[0][4]) / 60000


    return sommet