## Lab 2, Chart of km-miles
## Kaiya Provost

def km2milesChart(numbers):
    """Converts integer km values from (0 to numbers) and prints"""
    print("km"+"\t"+"miles")
    for km in range(numbers+1):
        miles = 0.621371*km
        print(str(km)+"\t"+str(miles))
km2milesChart(10)
