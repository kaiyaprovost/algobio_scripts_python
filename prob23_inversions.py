##def inversionCount(array):
##    inv = 0
##    for i in range(0,len(array)-1):
##        #print "i",i
##        j = i+1
##        while j < len(array):
##            if array[i] > array[j]:
##                inv += 1
##            j += 1
##    return inv

##def mergeSort(array,inv):
##    """
##    Takes a list and sorts it in place with merge sort
##    """    
##    n = len(array)
##    if n > 1:
##        mid = n//2
##        left = array[:mid]
##        right = array[mid:]
##        mergeSort(left,inv)
##        mergeSort(right,inv)
##        i=0
##        j=0
##        k=0
##        while i < len(left) and j < len(right):
##            print "left",left[i],"right",right[j]
##            print "inv",inv
##            if left[i] < right[j]:
##                array[k]=left[i]
##                i += 1
##            else:
##                print "inv!"
##                array[k]=right[j]
##                j += 1
##                inv += 1
##            k += 1
##        while i < len(left):
##            array[k]=left[i]
##            i += 1
##            k += 1
##        while j < len(right):
##            array[k]=right[j]
##            j += 1
##            k += 1
##    return array,inv

def mergeCount(listA,listB): ## A and B are sorted lists
    i = 0
    j = 0
    inv = 0
    OutList = []
    while i < len(listA) and j < len(listB):    ## not at end of a list
        #print "listA","listB"
        #print listA[i],listB[j]
        nextNum = min(listA[i],listB[j])
        OutList.append(nextNum)
        if listB[j] == nextNum:
            j = j + 1
            inv += len(listA) - i ##inc by num left in A
        else:
            i = i + 1
    while i < len(listA):
        OutList.append(listA[i])
        i = i + 1
    while j < len(listB):
        OutList.append(listB[j])
        j = j + 1
    #print "inv","outlist"
    #print inv,OutList
    return inv,OutList
    #return inv

def sortCount(listL):
    if len(listL) == 1:
        #print "single item"
        #print 0,listL
        return 0,listL
    else:
        n = len(listL)
        mid = n//2
        listA = listL[:mid]
        listB = listL[mid:]
        #print "split lists"
        #print listA,listB
        invA,sortedA = sortCount(listA)
        invB,sortedB = sortCount(listB)
        crossInv, sortedL = mergeCount(sortedA, sortedB)
        #print "after merge"
        #print (invA + invB + crossInv),sortedL
        return (invA + invB + crossInv),sortedL

##def inversionCount2(array):
##    copy = array[:]
##    sort = array[:]
##    sort = mergeSort(sort)
##    inv = 0
##    #print copy
##    #print sort
##    while len(copy) > 1:
##        find = copy[0]
##        loc = sort.index(find)
##        #print "find",find
##        #print "loc",loc
##        inv += loc
##        #print "inv",inv
##        copy.remove(find)
##        sort.remove(find)
##        #print copy
##        #print sort
##    return inv

def main():
    infile = open("C:/Users/Kaiya/Desktop/rosalind_inv.txt","rU")
    #infile = open("C:/Users/Kaiya/Desktop/scratch_rosalind.txt","rU")

    n = infile.readline()
    aList  = infile.readline()

    infile.close()

    n = n.strip()
    n = int(n)

    aList = aList.strip()
    aList = aList.split(" ")
    aList = [int(i) for i in aList]
    print "file read"
    #print "aList 0:5",
    #print aList[0:5]

    ans = sortCount(aList)

    print "inversions: ",
    print ans[0]

    outfile = open("C:/Users/Kaiya/Desktop/rosalind_inv_ans.txt","w")
    #outfile = open("C:/Users/Kaiya/Desktop/scratch_rosalind_2.txt","w")

    print >>outfile, ans[0]

    outfile.close()
    print "done"

if __name__ == "__main__":
    #import timeit
    #import random
    #array = [random.random() for i in range(3000)]
    #print(timeit.timeit("inversionCount(array)", setup="from __main__ import inversionCount,array", number=10))
    main()
