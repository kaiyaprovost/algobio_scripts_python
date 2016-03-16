import math
import matplotlib.pyplot as plt

## PART 1
x = range(1,101)

## How could you rewrite the above using list comprehensions? 

y1 = []
y1a = [math.log(i) for i in x]
y2 = []
y2a = [math.sqrt(i) for i in x]

for i in x:
    y1.append(math.log(i))
    y2.append(math.sqrt(i))

#print y1[0:5]
#print y1a[0:5]
#print y2[0:5]
#print y2a[0:5]

plt.plot(x,y1,label="y1 = log(x)")
plt.plot(x,y2,label="y2 = sqrt(x)")
plt.legend()

plt.show()
## sqrt grows faster

## PART 2

#plt is already imported
import numpy as np

a = np.array([2,3,4])
print a
b = np.array(range(100))
print b[0:5]
c = np.linspace(0,99,100)
print c[0:5]

x = np.linspace(1,100,100)
y1 = np.log(x)
y2 = np.sqrt(x)

plt.plot(x,y1,label="y1 = log(x), np")
plt.plot(x,y2,label="y2 = sqrt(x), np")
plt.legend()

plt.show()

## CHALLENGES

x = np.linspace(1,1001,1001)
y1 = np.log(x)
y2 = np.sqrt(x)

plt.plot(x,y1,"b--",label="y1 = log(x), np1000")
plt.plot(x,y2,"r:",label="y2 = sqrt(x), np1000")
plt.legend()

plt.show()

## at x = 1000, the sqrt function is larger

## PART 3

## scatter_plot.py creates a random assortment of N points from 0:1
## it also generates a random assortment of N colors from 0:1
## then it generates a random assortment of N areas of circles from 0:15
## and lastly it plots these things together

years = [2003,2004,2005,2006,2007,2008,2009,2010,2011]
ny = [5399,5100,5565,4460,4165,5741,4134,2385,3118]
nj = [2887,2698,3363,2432,3134,3214,4598,3320,3398]
ct = [1403,1348,1810,1788,3058,2738,2751,1964,2004]

## plt is already imported

plt.scatter(years,ny,c='r',marker="o",label="NY")
plt.scatter(years,nj,c='b',marker="o",label="NJ")
plt.scatter(years,ct,c='k',marker="o",label="CT")
plt.legend()
plt.title("Lyme Disease in NY, NJ, and CT")
plt.xlabel("Year")
plt.ylabel("Number of Cases")
plt.show()

## part 4

## plt and numpy are already imported
import csv

infile = open("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/statesSummary.csv","rU")
reader = csv.reader(infile)
yearLine = reader.next()
years = [int(w) for w in yearLine[1:]]

#print years

#for i in range(5):
for i in range(50):
    line = reader.next()
    stateName = line[0]
    stateValues = [int(w) for w in line [1:]]
    #color = np.random.rand(9)
    #color = (1.0,0.0,i/5.0)
    color = (np.random.rand(1),np.random.rand(1),np.random.rand(1))
    plt.scatter(years,stateValues,c=color,label=stateName)

plt.title("Cases of Lyme Disease")
plt.xlabel("Year")
plt.ylabel("Number of Cases")
plt.legend(loc = 2,fontsize = "x-small")
plt.show()

## part 5
## edited statesFilled goes here

infile = open("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/statesSummary.csv","rU")
reader = csv.reader(infile)
yearLine = reader.next()
years = [int(w) for w in yearLine[1:]]

stateNames = []
stateTotals = []
stateTotals2011 = []
stateTotalsDif = []

i = 0
for row in reader:
    #print row[-1]
    stateNames.append(row[0])
    #print stateNames[i]
    stateTotals.append(sum([int(r) for r in row[1:]])) ## for normal
    stateTotals2011.append(int(row[-1])) ## for 2011 only
    #print stateTotals[i]
    
    ## to do the net differences between:
    dif = int(row[-2]) - int(row[-1])
    if dif > 0:
        stateTotalsDif.append(dif)
    elif dif <= 0:
        stateTotalsDif.append(0) ## anyone who is negative, set to zero
    i = i + 1
    #print i

maxCases = float(max(stateTotals))
scaledTotals = [i/maxCases for i in stateTotals]

maxCases2011 = float(max(stateTotals2011))
scaledTotals2011 = [i/maxCases2011 for i in stateTotals2011]

maxCasesDif = float(max(stateTotalsDif))
scaledTotalsDif = [i/maxCasesDif for i in stateTotalsDif]

#print scaledTotals

## adding the edited statesFilled to edit it more

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

# create the map
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

# load the shapefile, use the name 'states'
#map.readshapefile('st99_d00', name='states', drawbounds=True)
map.readshapefile("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/st99_d00", name='states', drawbounds=True)

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca() # get current axes instance

## get state and draw the filled polygon

for i in range(len(stateNames)):
    seg = map.states[state_names.index(stateNames[i])]
    poly = Polygon(seg, facecolor=(1.0,abs(1-scaledTotals[i]),1.0),edgecolor=(1.0,abs(1-scaledTotals[i]),1.0))
    ax.add_patch(poly)

plt.show()

## make plots for the data for only the last year in the file 2011

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
map.readshapefile("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/st99_d00", name='states', drawbounds=True)
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])
ax = plt.gca()
for i in range(len(stateNames)):
    seg = map.states[state_names.index(stateNames[i])]
    poly = Polygon(seg, facecolor=(1.0,abs(1-scaledTotals2011[i]),1.0),edgecolor=(1.0,abs(1-scaledTotals2011[i]),1.0))
    ax.add_patch(poly)
plt.show()

## make a plot that shows the net increase in cases from 2010 to 2011

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
map.readshapefile("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/st99_d00", name='states', drawbounds=True)
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])
ax = plt.gca()
for i in range(len(stateNames)):
    seg = map.states[state_names.index(stateNames[i])]
    poly = Polygon(seg, facecolor=(1.0,abs(1-scaledTotalsDif[i]),1.0),edgecolor=(1.0,abs(1-scaledTotalsDif[i]),1.0))
    ax.add_patch(poly)
plt.show()

## normalize the data by population size, plot per capita (see fillstates.py)
popdensity = {
'New Jersey':  438.00,
'Rhode Island':   387.35,
'Massachusetts':   312.68,
'Connecticut':	  271.40,
'Maryland':   209.23,
'New York':    155.18,
'Delaware':    154.87,
'Florida':     114.43,
'Ohio':	 107.05,
'Pennsylvania':	 105.80,
'Illinois':    86.27,
'California':  83.85,
'Hawaii':  72.83,
'Virginia':    69.03,
'Michigan':    67.55,
'Indiana':    65.46,
'North Carolina':  63.80,
'Georgia':     54.59,
'Tennessee':   53.29,
'New Hampshire':   53.20,
'South Carolina':  51.45,
'Louisiana':   39.61,
'Kentucky':   39.28,
'Wisconsin':  38.13,
'Washington':  34.20,
'Alabama':     33.84,
'Missouri':    31.36,
'Texas':   30.75,
'West Virginia':   29.00,
'Vermont':     25.41,
'Minnesota':  23.86,
'Mississippi':	 23.42,
'Iowa':	 20.22,
'Arkansas':    19.82,
'Oklahoma':    19.40,
'Arizona':     17.43,
'Colorado':    16.01,
'Maine':  15.95,
'Oregon':  13.76,
'Kansas':  12.69,
'Utah':	 10.50,
'Nebraska':    8.60,
'Nevada':  7.03,
'Idaho':   6.04,
'New Mexico':  5.79,
'South Dakota':	 3.84,
'North Dakota':	 3.59,
'Montana':     2.39,
'Wyoming':      1.96,
'Alaska':     0.42,
"District of Columbia": 3832.65,
"Puerto Rico": 387.35}

infile = open("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/statesSummary.csv","rU")
reader = csv.reader(infile)
yearLine = reader.next()
years = [int(w) for w in yearLine[1:]]

stateNames = []
stateTotalsPop = []

i = 0
for row in reader:
    stateNames.append(row[0])
    allYearSum = (sum([int(r) for r in row[1:]]))
    #print allYearSum
    #print popdensity[stateNames[i]]
    popAdj = float(allYearSum) / float(popdensity[stateNames[i]])
    stateTotalsPop.append(popAdj)
    i = i + 1

maxCasesPop = float(max(stateTotalsPop))
scaledTotalsPop = [i/maxCasesPop for i in stateTotalsPop]

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
map.readshapefile("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/st99_d00", name='states', drawbounds=True)
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])
ax = plt.gca()
for i in range(len(stateNames)):
    seg = map.states[state_names.index(stateNames[i])]
    poly = Polygon(seg, facecolor=(1.0,abs(1-scaledTotalsPop[i]),1.0),edgecolor=(1.0,abs(1-scaledTotalsPop[i]),1.0))
    ax.add_patch(poly)
plt.show()