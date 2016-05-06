def adjList(edges):
    adjacency = {}
    for edge in edges:
        #print edge
        split = edge.split()
        first = int(split[0])
        second = int(split[1])
        if adjacency.get(first) == None:
            adjacency[first] = [[None],[second]]
        else:
            if adjacency[first][1] == [None]:
                adjacency[first][1] = [second]
            else:
                adjacency[first][1].append(second)
        if adjacency.get(second) == None:
            adjacency[second] = [[first],[None]]
        else:
            if adjacency[second][0] == [None]:
                adjacency[second][0] = [first]
            else:
                adjacency[second][0].append(first)
        #print first,second,adjacency
    return adjacency

def topSort(adjacency,linear=[]):
    short = adjacency
    for key in short:
        #print key,"key",
        parent = short[key][0]
        child = short[key][1]
        if parent == [None] or parent == []:
            ## HAS NO PARENTS
            #print key,"no parents"
            linear.append(key) ## add to linear list
            for kid in child:
                #print kid,"kid"
                if kid != None:
                    short[kid][0].remove(key) ## begin remove key from children's parents lists
                    #print "removed parent from kid"
                #else:
                    #print "no children"
                    #print "end of list"
            break
    if key in linear:
        del short[key]
        #print short,"new dict"
        print linear,"linear"
        if len(short) > 0:
            topSort(short,linear)
        return short,linear
    
def main():
    #print "hi"

    #infile = open("C:/Users/Kaiya/Desktop/scratch_rosalind.txt","rU")
    infile = open("C:/Users/Kaiya/Desktop/rosalind_ts.txt","rU")    
    firstLine = infile.readline()
    edges = infile.readlines()
    infile.close()

    nodes,numEdges = firstLine.strip().split()
    edges = [i.strip() for i in edges]

    adjacency = adjList(edges)

    #print adjacency

    #testAdj = {13: [[144], [826]], 41: [[92], [None]], 92: [[732], [41]], 114: [[993], [309, 144]], 144: [[114], [283, 367, 603, 13]], 156: [[283], [706]], 283: [[144], [156, 620]], 300: [[986], [None]], 309: [[114], [706]], 320: [[367], [None]], 367: [[144], [320, 393]], 372: [[993], [732, 438]], 377: [[820], [None]], 393: [[367], [None]], 438: [[732, 372], [None]], 603: [[144], [852, 986]], 620: [[283], [None]], 677: [[986], [None]], 706: [[156, 309], [None]], 732: [[372], [438, 92]], 820: [[993], [377]], 826: [[13], [None]], 852: [[603], [None]], 943: [[986], [None]], 986: [[603], [943, 677, 300]], 991: [[], [None]], 993: [[], [114, 820, 372]]}
    #new,sort = topSort(testAdj)

    new,sort = topSort(adjacency)
    #print new
    #print sort

    #outfile = open("C:/Users/Kaiya/Desktop/scratch_rosalind_2.txt","w")
    outfile = open("C:/Users/Kaiya/Desktop/rosalind_ts_ans.txt","w")

    for i in sort:
        print >>outfile, i,
    
    outfile.close()

if __name__ == "__main__":
    main()
