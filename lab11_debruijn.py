## try on small seqs
## try on two big seqs
## fix Composition
## fix graph connecter to search through the lists as well

def getReadsFromFile(infileString):
    f = open(infileString,"rU")
    #Depending on the file, could have extra newlines at end, strip off:
    data = f.read().rstrip()
    f.close()
    return data.split("\n")

def assemble(k_mers):
    """
    Takes k_mers and returns a sequence
    """
    g = createDeBruijnGraph(k_mers)
    print "The graph is: ", g     
    balanceGraph2(g)
    print "\nThe balanced graph is: ", g

    print "\n\nBuilding up the Eulerian cycle"
    c = eulerianCycle(g)
    print "\n\nFound the cycle:", c

    #convert the cycle c into the sequence:
    sequence = ""

    for i in range(1,len(c)):
        first = c[i-1]
        second = c[i]
        #print first,second,
        if first[1] == second[0]:
            #print "match"
            if sequence == "":
                sequence = sequence + str(first)+str(second[1])
            else:
                sequence = sequence + str(second[1])
        else:
            print "error"
            print "the kmer sequences do not overlap",
            print first,second
            sequence = sequence + str(first)+"//"+str(second)
    print "\nThe sequence is: ",sequence
    return sequence

def createDeBruijnGraph(reads):
    adjList = {}
    for read in reads:
        #prefix = read[0:2]
        prefix = read[0:-1]
        suffix = read[1:]
        #print "pre","suf"
        #print prefix,suffix
        if adjList.get(prefix) != None: ## if the prefix exists already
            adjList[prefix].append(suffix)
            #print "adjList",
            #print adjList
        else:
            adjList[prefix] = [suffix]
            #print "adjList[prefix]",
            #print adjList[prefix]
        if adjList.get(suffix) == None: ## if the suffix does not exist
            adjList[suffix] = []
            #print "adjList[suffix]",
            #print adjList[suffix]
    #print "keys",adjList.keys()
    #print "vals",adjList.values()
    for key in adjList:
        if [key] not in adjList.values():
            first = key
            break
    adjList[""] = [first]
    #print adjList
    return adjList

def balanceGraph2(g):
    for parent in g:
        if parent == "":
            #print "FIRST"
            firstNode = g[parent]
        if g[parent] == []:
            #print "LAST"
            lastNode = parent
            #print firstNode,lastNode
    g[lastNode] = firstNode
    del g[""]

def balanceGraph(g):
     """
     Add extra edges to g to make it "balanced"-- that is every
     node has the same incoming and outcoming edges.
     Will assume the g has a Hamiltonian path, so, only need to add in one edge.
     """
     #Make a single list of the nodes with in-coming edges:
     allNeighborLists = g.values()
     print allNeighborLists,"allLists"
     allNeighbors = [i for nList in allNeighborLists for i in nList]
     print allNeighbors,"all"

     #Find the node with no outgoing edges:
     for node in g.keys():
        #Find the node with no outgoing edges:
        print node,"node"
        print g[node],"gnode"
        if not g[node]:
           endNode = node
           print endNode,"end"
        #Find the node with no incoming edges:
        if g not in allNeighbors:
           begNode = node
           print begNode, "beg"
     #Attach them
     g[endNode] = [begNode]

def eulerianCycle(graph):
    """
    Form a cycle Cycle by randomly walking in Graph
    (don't visit the same edge twice!)
    """
    #Put all edges into the unexplored edges:
    unexplored = graph.copy()
    #Grab an edge from graph to start off the cycle:
    key, value = unexplored.popitem()
    #Use that as the start of our cycle:
    cycle = [key,value[0]]
    print "cycle",cycle
    print "unex",unexplored
    #Add back to the dictionary if there's > 1 outgoing edges
    if len(value) > 1:
        unexplored[key] = value[1:]

    #While there are unexplored edges in graph:
    while unexplored:
        #for i in range(5):
        print "Currently, cycle is: ", cycle
        print "\t unexplored is: ", unexplored
        #Check if you can go extend the cycle:
        if cycle[-1] in unexplored: 
            neighbors = unexplored.pop(cycle[-1])
            if len(neighbors) > 0:
                if len(neighbors) > 1:
                    #Put back the remaining unvisited edges:
                    unexplored[cycle[-1]] = neighbors[1:]
                #Add to cycle
                cycle.append(neighbors[0])
        #Select a node newStart in cycle with still unexplored edges.
        else:                   
            for i in range(len(cycle)):
                #print i, cycle
                if cycle[i] in unexplored:
                    neighbors = unexplored.pop(cycle[i])
                    if len(neighbors) > 0:
                        #Reorder cycle to put i at the end:
                        cycle = cycle[:i] + cycle[i:] 
                        if len(neighbors) > 1:
                            #Put back the remaining unvisited edges:
                            unexplored[cycle[-1]] = neighbors[1:]
                        #Add to cycle
                        cycle.append(neighbors[0])
                    break

    return cycle

def Composition(k,text):
    kmers = []
    for i in range(len(text)-k+1):
        #print i,text[i:i+k]
        kmers.append(text[i:i+k])
    kmers.sort()
    return kmers

def main():
    
##    #infileString = "C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/simpleReads.txt"
    infileString = "C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/textbookReads.txt"

    testfile = open(infileString,"rU")
    test = testfile.read()
    testfile.close()
    print test

    reads = getReadsFromFile(infileString)

    #print reads

    #adjList = createDeBruijnGraph(reads)
    #print adjList

    #balanceGraph(adjList)
    #print adjList

    #print eulerianCycle(adjList)

    #assemble(reads)

    #print "----------------------------"
    #print "the kmers are:",Composition(3,"TATGGGGTGC")

    #test = Composition(3,"ACCGAAGCT")
    print test
    print 

    #test = ["CCGAA","CGAAG","GAAGC","AAGCT","ACCGA"]
    g = createDeBruijnGraph(reads)
    print g
    balanceGraph2(g)
    print g
    #c = eulerianCycle(g)
    #print c

    assemble(test)

if __name__ == "__main__":
    main()
