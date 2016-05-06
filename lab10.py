import numpy as np
import matplotlib.pyplot as plt

cityNum = {}
cityNum["NYC"] = 0
cityNum["Chicago"] = 1
cityNum["Houston"] = 2
cityNum["San Jose"] = 3

flights = np.zeros( (4,4) )

flights[cityNum["NYC"],cityNum["Chicago"]] = 1
flights[cityNum["NYC"],cityNum["Houston"]] = 1
flights[cityNum["Chicago"],cityNum["NYC"]] = 1
flights[cityNum["Chicago"],cityNum["San Jose"]] = 1
flights[cityNum["Houston"],cityNum["NYC"]] = 1
flights[cityNum["Houston"],cityNum["San Jose"]] = 1
flights[cityNum["San Jose"],cityNum["Chicago"]] = 1
flights[cityNum["San Jose"],cityNum["Houston"]] = 1

#Create the self-loops:
for i in range(4):
    flights[i,i] = 1

print cityNum
print flights
print flights.dot(flights)
