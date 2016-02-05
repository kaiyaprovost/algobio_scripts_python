prob = open(r"C:/Users/Kaiya/Desktop/rosalind_gc.txt")
lines = prob.readlines()

##  if not > count c +g with accumulator
## if > set c + g back to 0
## how many bases in line - count all 4
## percent
## with name

## running max?

## get the number of specimens, or "chunks", to iterate over later 
def getChunks(lines):
    totalNames = 0
    for i in range(len(lines)):
        if lines[i][0] == ">":
            totalNames = 1 + totalNames
    return(totalNames)

countNames = 0 ## kern index
currentPercent = 0 ## the current percentage
countC = 0 ## counts of C, G, A, T respectively 
countG = 0
countA = 0
countT = 0
percentGC = [] 

## for this problem, get the number of chunks
totalNames = getChunks(lines)

names = list(range(totalNames)) ## sets a placeholder list the same length as the number of names
                                ## will be list of names of organisms, without the ">"

percentGC = list(range(totalNames)) ## list of percentGC, indexed the same as the organism names
                                    ## sets a placeholder list the same length as the number of percents

for i in range(len(lines)):
    if lines[i][0] == ">": ## if the string starts with a ">" it must be a name

    ## steps:
        ## fix old percentages
        ## update counter
        ## split names 

        if i != 0:    ## if it is not the first line, convert the current running total of percents to the final percent
            percentGC[countNames] = currentPercent
            print "final percent"
            print percentGC[countNames] ## list the current final percent
            print

        ## reset all counts to 0, as floats
        countC = 0.0
        countG = 0.0
        countA = 0.0
        countT = 0.0
        print("C","G","A","T")
        print(countC,countG,countA,countT)

        if i != 0: ## if it is not the first line, update the count of names
            countNames = countNames + 1
        print "count of names"
        print(countNames)

        names[countNames] = lines[i][1:].strip() ## set the matching index in the names list to the rest of the line containing the name
                                                ## without carat or white space
        
        print "line"
        print(names[countNames])

    else: ## if it is not a name, so it does not have a ">"
        print "line"
        print(lines[i].strip())
        countC = countC + lines[i].count("C") ## update all the counters with teh count of each base in the string
        countG = countG + lines[i].count("G")
        countA = countA + lines[i].count("A")
        countT = countT + lines[i].count("T")
        currentPercent = ((countC+countG)/(countC+countG+countA+countT)) * 100 ## calculate the current percent as given by those updated counts
        print("C","G","A","T")
        print(countC,countG,countA,countT)
        print "current percent"
        print currentPercent

        if i == (len(lines)-1): ## if it is the last line, update the current percent to the final percent
            percentGC[countNames] = currentPercent
            print "final percent"
            print percentGC[countNames]
            print

## start main part of function
print
print "names"
print names
print "percents"
print percentGC

## find the maximum of the GC percent lists
maxGC = max(percentGC)
print "max"
print maxGC

## get the index matching that GC percent
maxIndex = percentGC.index(maxGC)
print "max index"
print maxIndex
print
print "max name, max GC:"

## output the name and the percent that match the max GC percent
print names[maxIndex]
print maxGC

#prob.close()
