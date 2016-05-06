## copied dubruijn graphs file - in order, does not need cycle

def getReadsFromFile(infile):
	f = open(infile)
	#Depending on the file, could have extra newlines at end, strip off:
	data = f.read().rstrip()
	return data.split("\n")

def createDeBruijnGraph(reads):
	#Initialize a dictionary to hold the adjacency list.
	adjList = {}
	for read in reads:
		#print "read",
		#print read
		#Get the prefix and suffix:
		prefix = read[:-1]
		suffix = read[1:]
		#print "pre,suf",
		#print prefix,suffix
		if prefix in adjList:
			#It's in the list, and by construction, it's value is a list:
			adjList[prefix].append(suffix)
		else: #create a new entry for it:
			adjList[prefix] = [suffix]
		if suffix not in adjList:
			#Add it in with no outgoing neighbors:
			adjList[suffix] = []
	keyList = []
	for key in adjList:
		keyList.append(key)
	#print "KEYS",keyList
	valList = []
	for vals in adjList.values():
		for i in vals:
			valList.append(i)
	#print "VALUES",valList
	for key in keyList:
		if key not in valList:
			first = key
			break
	adjList[""] = [first]
	#print adjList        
	return adjList

if __name__ == "__main__":
    infileString = "C:/Users/Kaiya/Desktop/rosalind_ba3e.txt"
    reads = getReadsFromFile(infileString)

    graph = createDeBruijnGraph(reads)

    keys = graph.keys()
    keys.sort()

    outfile = open("C:/Users/Kaiya/Desktop/rosalind_ba3e_ans.txt","w")

    for key in keys:
        if key != "" and graph[key] != []:
            print >>outfile, key,"->",
            #print key,"->",
            if len(graph[key]) == 1:
                print >>outfile, graph[key][0]
                #print graph[key][0]
            else:
                print >>outfile, ",".join(graph[key])
                #print ",".join(graph[key])

    outfile.close()


