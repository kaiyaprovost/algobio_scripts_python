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

infile = open("C:/Users/Kaiya/Desktop/rosalind_ms.txt","rU")

n = infile.readline()
array = infile.readline()

infile.close()

n = int(n.strip())
array = array.split()
array = [int(x) for x in array]

mergeSort(n,array)

#print array

outfile = open("C:/Users/Kaiya/Desktop/rosalind_ms_ans.txt","w")

for i in array:
    print >>outfile, i,

outfile.close()
