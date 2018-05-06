import matplotlib.pylab as plt
import pandas as pd
import geopandas as gpd

# data can be important from Henrikki Tenkanen tutorial
# let's import a shape file

def plot_shp(shpfile, c='b'):
    data= gpd.read_file(shpfile)
    return data.plot(color=c)

plt0=plot_shp("/home/houcemeddine/my_git/open_maps/PyGeo/Data/TUN_adm0.shp", c="k")
plt1=plot_shp("/home/houcemeddine/my_git/open_maps/PyGeo/Data/TUN_adm1.shp", c='k')
plt2=plot_shp("/home/houcemeddine/my_git/open_maps/PyGeo/Data/TUN_adm2.shp", c='k')
plt.show()

# let us generate the area of each delegation.
# each delegation corresponds to a polygons
# geopandas stores polygons into a Shapely object (another python module used by Geopandas)

print data["geometry"][0:3]
