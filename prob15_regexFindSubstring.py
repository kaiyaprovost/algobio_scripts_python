infile = open("C:/Users/Kaiya/Desktop/rosalind_ba1d.txt","r")
lines = infile.readlines()
infile.close()

string = lines[1].strip()
sub = lines[0].strip()

##print sub
##print string

import re

#finds = re.search(sub,string)

#print finds.start()

##point = 0
##listFound = []
##finds = ""
##while point <= len(string)-len(sub):
##    #print string[point]
##    finds = re.search(sub,string[point:])
##    if finds.start() == None:
##        print "done"
##    else:
##        print finds.start()
##    point = point + 1

## re.search.start()

count = 0
found = []
finds = ""

outfile = open("C:/Users/Kaiya/Desktop/rosalind_ba1d_out.txt","w")

for i in range(len(string)-len(sub)):
    newstring = string[i:]
    finds = re.search(sub,newstring)
    #print finds.start()
    if finds != None:
        if finds.start() == 0:
            found.append(i)

for j in found:
    print >>outfile, j,

outfile.close()

##finds = re.finditer(sub,string)
##for match in finds:
##    print match.start()
