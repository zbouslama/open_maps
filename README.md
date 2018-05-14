# open_maps
### project description
Scientists draw full benefit from their raw data by performing complex data analysis. Creating maps is an essential component to associate meaningful interpretation to data.
Research groups in low income countries suffer from budget restrictions due to several economical and political issues and can't afford purchasing licenses for non academic GIS (Geographic Information Systems) software neither following specific GIS softaware trainings.
Open license GIS softwares are available and offer a large set of options. However, their use is not trivial and require intensive training sessions.
###
The aim of this project, is to offer an open, user friendly alternative to these tools and will be accessible to GIS and non GIS users and its use won't require any programming experience. It will allow the targeted users to spend more time on curating and analyzing their data rather than setting up complex environments, fetching appropriate map format, converting their data accordingly and debugging.

Open maps will offer interactive visualization of scientific data projected on 2D maps. It will be developped based on the use of open packages such as Python libraries.
Users will be able to upload their raw data files containing spatio-temporal measurements, explore them interactively and generate graphics and reports on a “what you see is what you get” basics.

### Important concepts
#### Simplicity
We embrace simplicity at all the levels of the project. This implies at first that the users will be able to make use of the application via a web server without the need to install it on their machines. A very comprehensive example, explaining how to implement a web server with python can be found [here](https://ruslanspivak.com/lsbaws-part1/)

#### Interactivity
Geographical data are better handled using exploratory tools to discover new spatial-temporal patterns. More often, exploratory analysis is interactive. There are several python packages which could be used to generate interactive maps (see examples [here](https://plot.ly/python/ipython-notebook-tutorial/) and [here](https://blog.modeanalytics.com/python-interactive-plot-libraries/)). Interactive maps can be easily [web implemented](http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/).

#### Usage of the application
We want the users to achieve their desired analysis quickly with very simple steps:
    1- select the map.
    2- upload the data.
    3- run the analysis.
    4- Explore the output.
    5- download the reports.

#### Why Python ?
Python by itself is a general purpose open source programming language. It is very easy to learn and is backed by a highly active community. Recently it becomes one of the most important tools among data scientists offering a lots of packages to manage data ([pandas](https://pandas.pydata.org/)),  run numerical analysis ([numpy](http://www.numpy.org/)) and predictive models ([scikit-learn](http://scikit-learn.org/stable/)), generate graphs and plots ([matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/)) and to interact with the code and the data ([ipython](https://ipython.org/) and [jupyter](http://jupyter.org/)).

## Packages
GIS modules in python has been progressing extensively. We already tested some scripts for some basic GIS data handling and plotting. An example might be found in [PyGeo](https://github.com/zbouslama/open_maps/tree/master/PyGeo) foler. Noticing that we found some issues with Python3.6 for geopandas and Bokeh. Therefore, we recommand using Python2.7.

Please do not use conda for the installation because of the risk of the channels confusion. Instead use pip as follows.

```sh
$ pip install PACKAGE
```
where PACKAGE:
  * [geopandas](http://geopandas.org/), _open source project to make working with geospatial data in python easier_.
  * [Bokeh](https://bokeh.pydata.org/en/latest/), To make interactive plots in web browsers.
  * [HoloViews](https://bokeh.pydata.org/en/latest/), For simpler handling of interactive plots (built on top of Bokeh).
  * [Geoviews](http://geo.holoviews.org/#), a python library that includes interactive geospacial tools. 
  
# PROGRESS
We started implementing source codes for our project.
GIS Package used : FOLIUM.
We created HTML page that includes our programme via FLASK package on Python.
We were able to create a page that uploads a CSV file.
we created a script that allows to plot dots on a map. Lat long coordinates uploaded from a CSV file. Layer map generated from openstreetmaps.
Now, we would like to link the two scripts so that everything will be done via online web app.



