## copied dubruijn graphs file - in order, does not need cycle

def Composition(k,text):
	kmers = []
	for i in range(len(text)-k+1):
		#print i,text[i:i+k]
		kmers.append(text[i:i+k])
		#kmers.sort()
	return kmers

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
    infileString = "C:/Users/Kaiya/Desktop/rosalind_ba3d.txt"
    infile = open(infileString,"rU")
    k = infile.readline()
    text = infile.readline()
    infile.close()

    k = int(k.strip())
    text = text.strip()

    reads = Composition(k,text)

    graph = createDeBruijnGraph(reads)

    keys = graph.keys()
    keys.sort()

    outfile = open("C:/Users/Kaiya/Desktop/rosalind_ba3d_ans.txt","w")

    for key in keys:
        if key != "" and graph[key] != []:
            print >>outfile, key,"->",
            if len(graph[key]) == 1:
                    print >>outfile, graph[key][0]
            else:
                print >>outfile, ",".join(graph[key])

    outfile.close()


