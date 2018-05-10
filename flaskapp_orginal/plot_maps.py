import folium
import numpy as np 
import pandas as pd 

data=pd.read_csv("/home/houcemeddine/Desktop/test_geo_1.csv", sep=';', header=None)


maxLon=np.max( data[3] )
minLon=np.min ( data[3] )
maxLat=np.max( data[4] )
minLat=np.min ( data[4] )

def plot_point():
    m = folium.Map(
        location=[maxLon , minLat],
        tiles='Stamen Toner',
        zoom_start=13
    )
    for lon, lat in zip(data[3], data[4]):
        fcirc=folium.Circle(radius=3000, location=[lat, lon], popup='The Waterfront', color='crimson', fill=False )
        fcirc.add_to(m)
    return m
        

m=plot_point()
