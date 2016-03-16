# Lab 2: Converter Program
# Kaiya Provost, 27 Jan 2016

def km2miles(km):
    """ Given dist in km, outputs miles """
    ## distance in km is passed into the function
    miles = km*0.621371 # calculate distance in miles (0.621371*km)
    return(miles) # output distance in miles
    
km = 10

miles = km2miles(km)
print(miles)
