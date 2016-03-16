## pass info to next one to call it


##def printElementsRecursion(list,i):  
##    if i >= len(list):
##        return
##    print list[i]
##    printElementsRecursion(list,i+1)
##    print i

#listed = [7, 1, 3, 3, 2]

#printElementsRecursion(listed, 0)

x = int(input("number "))

def fibb(end):
    if end <= 1:
        return end
    return (fibb(end-1) + fibb(end-2))

print fibb(x)
