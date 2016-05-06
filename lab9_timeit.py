if __name__ == '__main__':
    import timeit
    import lab9_sort

    ## SELECTION, 100 SORT
    #print "Time for selection on sorted list of first 100 ints:"
    #print(timeit.timeit("sortList(getInputFirstN(100))", setup="from lab9_sort import sortList,getInputFirstN", number=1000))

    #print "Time for selection on sorted list of first 100 ints in rev order:"
    #print(timeit.timeit("sortList(getInputRevN(100))", setup="from lab9_sort import sortList,getInputRevN", number=1000))

    #print "Time for selection on sorted list of 100 random floats:"
    #print(timeit.timeit("sortList(getInputRandN(100,0,1))", setup="from lab9_sort import sortList,getInputRandN", number=1000))

    ## SELECTION, 10000 SORT
    print "Time for selection on sorted list of first 10000 ints:"
    print(timeit.timeit("sortList(getInputFirstN(10000))", setup="from lab9_sort import sortList,getInputFirstN", number=100))

    print "Time for selection on sorted list of first 10000 ints in rev order:"
    print(timeit.timeit("sortList(getInputRevN(10000))", setup="from lab9_sort import sortList,getInputRevN", number=100))

    print "Time for selection on sorted list of 10000 random floats:"
    print(timeit.timeit("sortList(getInputRandN(10000,0,1))", setup="from lab9_sort import sortList,getInputRandN", number=100))

    ## MERGE, 100 SORT
    #print "Time for merge on sorted list of first 100 ints:"
    #print(timeit.timeit("mergeSort(getInputFirstN(100))", setup="from lab9_sort import mergeSort,getInputFirstN", number=1000))

    #print "Time for merge on sorted list of first 10000 ints in rev order:"
    #print(timeit.timeit("mergeSort(getInputRevN(100))", setup="from lab9_sort import mergeSort,getInputRevN", number=1000))

    #print "Time for merge on sorted list of 100 random floats:"
    #print(timeit.timeit("mergeSort(getInputRandN(100,0,1))", setup="from lab9_sort import mergeSort,getInputRandN", number=1000))
    
    ## MERGE, 10000 SORT
    #print "Time for merge on sorted list of first 10000 ints:"
    #print(timeit.timeit("mergeSort(getInputFirstN(10000))", setup="from lab9_sort import mergeSort,getInputFirstN", number=100))

    #print "Time for merge on sorted list of first 100 ints in rev order:"
    #print(timeit.timeit("mergeSort(getInputRevN(10000))", setup="from lab9_sort import mergeSort,getInputRevN", number=100))

    #print "Time for merge on sorted list of 100 random floats:"
    #print(timeit.timeit("mergeSort(getInputRandN(10000,0,1))", setup="from lab9_sort import mergeSort,getInputRandN", number=100))
 
