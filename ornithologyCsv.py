import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

## read file
cardfile = open("C:/Users/Kaiya/Desktop/card_python.csv")
reader = csv.DictReader(cardfile)

## extract lat/long and ID
latStrings = []
longStrings = []
ident = []

for row in reader:
    if row["LATITUDE"] != "" :
        latStrings.append(row["LATITUDE"])
        longStrings.append(row["LONGITUDE"])
        ident.append(row["IDENTIFICATION"])

cardfile.close()

#for i in range(len(latStrings)):
#    print ident[i],"\t",latStrings[i],"\t",longStrings[i]


## convert to decimal degrees
# Decimal Degrees = Degrees + minutes/60 + seconds/3600

latDegStrings = []
longDegStrings = []

for lat in latStrings:
    latBreak = lat.split()
    first = float(latBreak[0])
    minute = float(latBreak[1])
    second = latBreak[2]
    direct = latBreak[-1]
    if second == direct:
        second = 0.0
    else:
        second = float(second)
    minConv = minute/60
    secConv = second/3600
    latDeg = first + minConv + secConv
    if direct == "N":
        latDeg = latDeg
    elif direct == "S":
        latDeg = latDeg * -1
    else:
        print "error"
    latDegStrings.append(latDeg)
    print latDeg

for lon in longStrings:
    lonBreak = lon.split()
    first = float(lonBreak[0])
    minute = float(lonBreak[1])
    second = lonBreak[2]
    direct = lonBreak[-1]
    if second == direct:
        second = 0.0
    else:
        second = float(second)
    minConv = minute/60
    secConv = second/3600
    lonDeg = first + minConv + secConv
    if direct == "E":
        lonDeg = lonDeg
    elif direct == "W":
        lonDeg = lonDeg * -1
    else:
        print "error"
    longDegStrings.append(lonDeg)
    print lonDeg   

## the below are the lat longs from my data to center on
#-97.85 = sum(longDegStrings)/len(longDegStrings)
#-111.6 = min(longDegStrings)
#-72.76 = max(longDegStrings)

# 29.74 = sum(latDegStrings)/len(latDegStrings)
# 21.52 = min(latDegStrings)
# 42.06 = max(latDegStrings)

## create the basemap (multiple versions included)
#m = Basemap()
#m = Basemap(projection="ortho",lat_0=45,lon_0=-100,resolution="l")
m = Basemap(llcrnrlat=15,urcrnrlat=50,llcrnrlon=-120,urcrnrlon=-60,lat_ts=30)
#m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
#m.drawcoastlines()
#m.fillcontinents(color="darkgreen",lake_color="lightblue")
#m.drawmapboundary(fill_color="darkblue")
#m.fillcontinents(color="hotpink",lake_color="yellow")
#m.drawmapboundary(fill_color="goldenrod")
m.shadedrelief()
#m.drawparallels(np.arange(-90.,120.,30.))
#m.drawmeridians(np.arange(0.,360.,60.)) 
m.drawparallels(np.arange(-90.,120.,10.))
m.drawmeridians(np.arange(0.,360.,15.)) 

#m.bluemarble()
x,y = m(longDegStrings,latDegStrings)
m.plot(x,y,'ro',markersize=10)

plt.show()