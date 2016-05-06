infile = open("C:/Users/Kaiya/Desktop/rosalind_seto.txt","rU")
n = int(infile.readline())
setA = infile.readline()
setB = infile.readline()
infile.close()

##print n
##print setA
##print setB

setA = set([int(i) for i in setA.strip().strip("{").strip("}").split(", ")])
setB = set([int(i) for i in setB.strip().strip("{").strip("}").split(", ")])

##print setA
##print setB
##print 

## give: AUB, ANB, A-B, B-A,Ac,Bc
## where Ac = U - A
## and U = {1,2,3...n}

AUB = list(setA.union(setB))

ANB = list(setA.intersection(setB))

AminB = list((setA - setB))

BminA = list((setB - setA))

##print AUB
##print ANB
##print AminB
##print BminA 

setU = set([i for i in range(1,n+1)])

AC = list((setU - setA))

BC = list((setU - setB))

##print AC
##print BC
##print

def setPrint(setList,outfile):
    for i in range(len(setList)):
        if i == 0:
            print >>outfile, "{"+str(setList[i])+",",
        elif i == len(setList)-1:
            print >>outfile, str(setList[i])+"}"
        else:
            print >>outfile, str(setList[i])+",",

outfile = open("C:/Users/Kaiya/Desktop/rosalind_seto_ans.txt","w")

setPrint(AUB,outfile)
setPrint(ANB,outfile)
setPrint(AminB,outfile)
setPrint(BminA,outfile)
setPrint(AC,outfile)
setPrint(BC,outfile)

outfile.close()
