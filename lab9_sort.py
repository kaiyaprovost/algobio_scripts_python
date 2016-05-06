def getInputList():
    """
    No inputs
    Returns the list to sort
    """
    s = raw_input("Please enter a list of ints, separated by spaces: ")
    a = [int(w) for w in s.split()]
    return a

def getInputFirstN(n):
    """
    Input N, output numbers 0 to n-1
    Returns the list to sort
    """
    aList = [i for i in range(0,n)]
    return aList

def getInputRevN(n):
    """
    Input N, output numbers n-1 to 0
    Returns the list to sort
    """
    aList = [i for i in range(n-1,-1,-1)]
    #print aList
    return aList

def getInputRandN(n,a,b):
    """
    Input N,A,B output N numbers between A and B such that a<= number <= B
    Returns the list to sort
    """
    import random
    aList = [random.uniform(a,b) for i in range(0,n)]    
    #print aList
    return aList
	
def sortList(aList):
    """
    Takes a list and sorts it in place with selection sort
    """
    #For each i, starting at len(aList)-1 and decrementing to 1.
    for i in range(len(aList)-1,0,-1):
        #Find the index of the largest element in the list aList[0:i+1]
        maxNum = max(aList[0:i+1])
        maxPos = aList.index(maxNum)
        #Swap the largest element with the element at position i.
        aList[maxPos],aList[i] = aList[i],aList[maxPos]
	
def printList(b):
    """
    Prints sorted list.
    No outputs
    """

    #print "The sorted list is:"
    #print b

def mergeSort(array):
    """
    Takes a list and sorts it in place with merge sort
    """    
    n = len(array)
    if n > 1:
        mid = n//2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i=0
        j=0
        k=0        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k]=left[i]
                i += 1
            else:
                array[k]=right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k]=left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1
    return array

def sortListInsert(a):
    """
    Takes a list and sorts it in place with insertion sort
    """        
    for i in range(1,len(a)):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j],a[j-1] = a[j-1],a[j]
            j += -1                   

def main():
    #print "Welcome to the sorting program!"
    #Get list of items to sort.
    #a = getInputList()
    #Get first N numbers to sort
    #a = getInputFirstN(100)
    #Get first N numbers in reverse order to sort
    #a = getInputRevN(100)
    #Get N random numbers between A and B
    a = getInputRandN(10000,0,10)
    
    #Sort list with selection sort.
    #sortList(a)
    #Sort list with merge sort.
    #a = mergeSort(a)
    #Sort list with insertion sort.
    sortListInsert(a)
    
    #Print sorted list
    printList(a)

if __name__ == "__main__":
    main()
