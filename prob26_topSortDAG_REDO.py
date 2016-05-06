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

def topSort2(adjacency):
    ## find all parents
    ## add to list
    ## pick one parent
    ## remove it
    ## check if the kids are parents
    ## if so add to list
    ## repeat

    nodeList = []
    linear = []

    short = adjacency
    for key in short:
        #print "key",key
        #print short[key]
        if short[key][0] == [None] or short[key][0] == []:
            #print key,"no parent"
            nodeList.append(key)
    for parent in nodeList:
        print "parent",parent
        linear.append(parent)
        for child in short[parent][1]:
            #print child,type(child),
            if child != None:
                if short[child][0] != [None] or short[child][0] != [] or short[child][0] != None:
                    short[child][0].remove(parent)
                    if short[child][0] == None or short[child][0] == []:
                        nodeList.append(child)
                else:
                    if short[child][0] == None or short[child][0] == []:
                        nodeList.append(child)                
        #print "startover"       
    return linear

    
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

    sort = topSort2(adjacency)
    #print new
    #print sort

    #outfile = open("C:/Users/Kaiya/Desktop/scratch_rosalind_2.txt","w")
    outfile = open("C:/Users/Kaiya/Desktop/rosalind_ts_ans.txt","w")

    for i in sort:
        print >>outfile, i,
    
    outfile.close()

if __name__ == "__main__":
    main()
