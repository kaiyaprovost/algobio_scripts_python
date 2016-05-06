def mergeSort(n,array):
    x = ""
    if n > 1:
        mid = n//2
        left = array[:mid]
        right = array[mid:]
        mergeSort(len(left),left)
        mergeSort(len(right),right)
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

def inversionLessThan(n,array):
    inv = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                if array[i] > array[j]:
                    inv += 1
    return inv

## finding a min element in a list?
## merge sort the list - look through it, find the minimum
## work out how you'd do it, in order vs not 

## merge sort the list, keep both sortted and not
## because merge sorted, the minimum is at the front of the list
## find original location of minimum
## add the index to the number of inversions
## delete the minimum from both lists
## repeat

def inversionCount(n,array):
    inv = 0
    copyList = array[:]
    sortList = array[:]
    mergeSort(n,sortList)

    #print "sortList",sortList
    while len(sortList) > 0:
        #print len(sortList),inv,"//",
        smallest = sortList[0]
        #print "smallest",smallest
        lookup = int(copyList.index(smallest))
        #print "where is smallest",lookup
        inv = inv + lookup
        #print "inv",inv
        sortList.remove(smallest)
        copyList.remove(smallest)
        #print "sortlist",sortList
        #print "copylist",copyList
    return inv   

def main():
    from datetime import datetime
    a = datetime.now()
    print a
    
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
    print "aList 0:5",
    print aList[0:5]

    ans = inversionCount(n,aList)

    print "inversions: ",
    print ans

    outfile = open("C:/Users/Kaiya/Desktop/rosalind_inv_ans.txt","w")
    #outfile = open("C:/Users/Kaiya/Desktop/scratch_rosalind_2.txt","w")

    print >>outfile, ans

    outfile.close()
    print "done"
    b = datetime.now()
    c = b - a
    print c

if __name__ == "__main__":
    main()
