def sortMinPart(aList,k,n):
    """
    Takes a list and sorts it in place with selection sort
    """
    bList = aList
    minList = []
    for i in range(k):
        minNum = min(bList)
        minList.append(minNum)
        bList.remove(minNum)
    return minList

n = 10
aList = [4,-6,7,8,-9,100,12,13,56,17]
k = 3

infile = open("C:/Users/Kaiya/Desktop/rosalind_ps.txt","rU")

n = infile.readline()
aList = infile.readline()
k = infile.readline()

infile.close()

n = n.strip()
n = int(n)

aList = aList.strip()
aList = aList.split(" ")
aList = [int(i) for i in aList]

k = k.strip()
k = int(k)

outList = sortMinPart(aList,k,n)

outfile = open("C:/Users/Kaiya/Desktop/rosalind_ps_ans.txt","w")

for i in outList:
    print >>outfile, i,

outfile.close()
