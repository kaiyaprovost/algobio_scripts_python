import random
import math

def welcome():
    print("This program computes wind chill for temps 20 to -25 degF")
    print("in intervals of 5, and for winds 5 to 50mph in intervals of 5")

def computeWindChill(temp,wind):
    ## input the formula, replacing T with temp and W with wind
    wchill = 35.74 + 0.6215*temp - 35.75*(wind**0.16) + 0.4275*temp*(wind**0.16) 
    return(wchill)

def main():
    welcome()                       #Print a message that explains what your program does
   
    #Print table headings:
    for temp in range(20, -25, -5): 
        print "\t",str(temp), 
    print
        

    #Print table:   
    for wind in range(5,55,5):      #For wind speeds between 5 and 50 mph
        print wind,"\t",            #Print row label 
        for temp in range(20, -25, -5): #For temperatures between 20 and -20 degrees
            wchill = computeWindChill(temp, wind)
            print wchill,"\t",      #Print the wind chill, separated by tabs
        print                       #Start a new line for each temp

main()
