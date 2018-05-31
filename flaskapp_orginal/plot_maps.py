import folium
import numpy as np 
import pandas as pd 
from scipy.spatial import distance

data=pd.read_csv("./data/data.csv", sep=';', header=None)

maxLon=np.max( data[3] )
minLon=np.min ( data[3] )
maxLat=np.max( data[4] )
minLat=np.min ( data[4] )

def centerpoint(Lon, Lat):
    maxLon = np.max( Lon )
    minLon = np.min ( Lon )
    maxLat = np.max( Lat )
    minLat = np.min ( Lat )
    minmax= [minLat, maxLon]
    maxmin= [maxLat, minLon ]
    maxmax= [maxLat, maxLon ]
    
    disLatHalf = ( distance.euclidean(maxmax,maxmin) )/2
    disLongHalf = ( distance.euclidean(maxmax,minmax) )/2
    centerLat= maxLat - disLatHalf
    centerLon= maxLon - disLongHalf
    return centerLat,  centerLon


def plot_point(longitude, latitude):
    a, b = centerpoint( longitude, latitude )
    m = folium.Map(
        location=[a , b],
        tiles='stamentoner',
        zoom_start=6
    )
    for lon, lat in zip(longitude , latitude ):
        fcirc=folium.Circle(radius=3000, location=[lat, lon], popup='The Waterfront', color='crimson', fill=False )
        fcirc.add_to(m)
    return m
        
def executeData():
    m=plot_point(data[3], data[4])
    m.save('./templates/maps.html')