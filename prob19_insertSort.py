def insertionSort(a,n):
    swap = 0
    for i in range(n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j-1],a[j] = a[j],a[j-1]
            swap +=1
            j += -1
            #print a, swap
    return swap

file = open("C:/Users/Kaiya/Desktop/rosalind_ins.txt","rU")
n = file.readline()
a = file.readline()


n = int(n.strip())
a = a.split()
a = [int(x) for x in a]

print n
print a

print insertionSort(a,n)


            
        
