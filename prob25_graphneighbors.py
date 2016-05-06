def connections(edges):
    tempDict = {}
    for edge in edges:
        split = edge.split()
        first = int(split[0])
        second = int(split[1])

        tempDict[first] = tempDict.get(first,0) + 1
        tempDict[second] = tempDict.get(second,0) + 1
    return tempDict

def main():
    print "hi"

    #infile = open("C:/Users/Kaiya/Desktop/scratch_rosalind.txt","rU")
    infile = open("C:/Users/Kaiya/Desktop/rosalind_deg.txt","rU")
    
    firstLine = infile.readline()
    edges = infile.readlines()
    infile.close()

    edges = [i.strip() for i in edges]
    outDict = connections(edges)

    print sorted(outDict)

    #outfile = open("C:/Users/Kaiya/Desktop/scratch_rosalind_2.txt","w")
    outfile = open("C:/Users/Kaiya/Desktop/rosalind_deg_ans.txt","w")

    for i in sorted(outDict):
        print >>outfile, outDict.get(i),
    
    outfile.close()

if __name__ == "__main__":
    main()
