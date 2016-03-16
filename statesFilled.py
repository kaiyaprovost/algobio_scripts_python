# Abbreviated version of basemap example (from stackoverflow: http://stackoverflow.com/questions/7586384/color-states-with-pythons-matplotlib-basemap)

import matplotlib.pyplot as plt
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

# get Texas and draw the filled polygon
seg = map.states[state_names.index('Texas')]
poly = Polygon(seg, facecolor='red',edgecolor='red')
ax.add_patch(poly)

# get New York and draw the filled polygon
seg = map.states[state_names.index('New York')]
poly = Polygon(seg, facecolor='blue',edgecolor='blue')
ax.add_patch(poly)

## get Vermont and NJ and draw the filled polygon

seg = map.states[state_names.index("Vermont")]
poly = Polygon(seg, facecolor="green",edgecolor="green")
ax.add_patch(poly)

seg = map.states[state_names.index("New Jersey")]
poly = Polygon(seg, facecolor="purple",edgecolor="purple")
ax.add_patch(poly)

plt.show()