import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from major_us_city_dma_codes import *

"""
Takes coordinates from outside file and puts in dictionary to use later:
"""
cityCoords = {}
for i in range(len(major_cities)):
     cityCoords[major_cities[i]['city']] = (major_cities[i]['latitude'],major_cities[i]['longitude'])


"""
Sets up a map of the US to draw on:
"""
m = Basemap(llcrnrlon=-125,llcrnrlat=15,\
            urcrnrlon=-50,urcrnrlat=50,\
            projection='tmerc',\
            lon_0=-90.,lat_0=35.)
m.drawcountries()
m.drawcoastlines()
m.drawstates()


"""
Set up a dictionary, so, we don't have to remember which cities
are assigned which indices for the matrix:
"""
cityNum = {}
cityNum["New York"] = 0
cityNum["Chicago"] = 1
cityNum["Houston"] = 2
cityNum["San Jose"] = 3

flights = np.zeros( (4,4) )
flights[cityNum["New York"],cityNum["Chicago"]] = 1
flights[cityNum["New York"],cityNum["Houston"]] = 1
flights[cityNum["Chicago"],cityNum["New York"]] = 1
flights[cityNum["Chicago"],cityNum["New York"]] = 1
flights[cityNum["Houston"],cityNum["New York"]] = 1
flights[cityNum["Houston"],cityNum["San Jose"]] = 1
flights[cityNum["San Jose"],cityNum["Chicago"]] = 1
flights[cityNum["San Jose"],cityNum["Houston"]] = 1
for i in range(4): flights[i,i] = 1



"""
Get the coordinates just for the cities in the example above
and plot to the screen:
"""
lons = []
lats = []
for city in sorted(cityNum.keys()):
     lats.append(cityCoords[city][0])
     lons.append(cityCoords[city][1])
x,y = m(lons,lats)
#Make dots large enough to see (and red):
m.scatter(x,y,40,marker='o', color='r')
#Label the cities:
for label, xpt, ypt in zip(sorted(cityNum.keys()),x,y):
     plt.text(xpt,ypt,label)

"""
Next, let's display each edge in our array:
"""
for c1 in cityNum.keys():
     for c2 in cityNum.keys():
          if c1 != c2 and flights[cityNum[c1],cityNum[c2]] > 0:
               #Get city coordinates:
               c1lat,c1lon = cityCoords[c1]
               c2lat,c2lon = cityCoords[c2]
               print c1, c1lon, c1lat, c2, c2lat,c2lon
               #Draw edge between them:
               m.drawgreatcircle(c1lon,c1lat,c2lon,c2lat,linewidth=2,color='b')

"""
Display the final product:
"""
plt.show()

