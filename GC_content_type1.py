prob = open("C:/Users/Kaiya/Desktop/scratch_rosalind_2.txt","r")

## fasta get names
def namesFasta(filename):
    """Gets the names from a fasta file"""
    names = []
    name_count = 0
    names_index = []
    filename.seek(0)
    all_lines = filename.readlines()
    for i in range(len(all_lines)):
        if all_lines[i][0] == ">":
            names.insert(name_count,all_lines[i][1:].strip())
            names_index.insert(name_count,i)
            name_count = name_count + 1
    filename.seek(0)
    return(names,names_index)

##  if not > count c +g with accumulator
## if > set c + g back to 0
## how many bases in line - count all 4
## percent
## with name

def dataFasta(filename):
    """Uses namesFasta to get the data out"""
    x = namesFasta(filename)
    indexes = x[1]
    all_lines = filename.readlines()
    ratio = indexes[-1] - indexes[-2]
    chunks = len(all_lines)/ratio
    data = []
    temp = ""
    concat = ""
    chunk_count = 0
    for i in range(len(all_lines)):
        temp = all_lines[i].strip()
        if i not in indexes:
            if i == (len(all_lines)-1):
                concat = concat + temp
                data.insert(chunk_count,concat)
                #print "verylast"
            elif all_lines[i+1][0] == ">":
                concat = concat + temp
                data.insert(chunk_count,concat)
                chunk_count = chunk_count + 1
                concat = ""
                #print "endchunk"
            else:
                concat = concat + temp
                #print "notlast"
    return data

def getGC(data):
    """Return the percent GC content of a string"""
    percents = []
    for i in range(len(name)):
        tempGC = data[i]
        lengthGC = float(len(tempGC))
        countGC = float(tempGC.count("G") + tempGC.count("C"))
        propGC = countGC / lengthGC
        percents.insert(i,propGC)
    return percents


def getMaxGC(name,data):
    """Get the maximum GC content name and percent"""
    contentGC = getGC(data)
    maxGC = max(contentGC)
    maxIndex = contentGC.index(maxGC)
    return (name[maxIndex],maxGC)

name = namesFasta(prob)[0]
data = dataFasta(prob)

maxGC = getMaxGC(name,data)
print maxGC[0]
print maxGC[1]*100

prob.close()


