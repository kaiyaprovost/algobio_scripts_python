## recopied from lab material
"""
Lab 11 Demonstration:  Assembling reads using deBruijn graphs
"""

def getReadsFromFile(infile):
	f = open(infile)
	#Depending on the file, could have extra newlines at end, strip off:
	data = f.read().rstrip()
	return data.split("\n")

def createDeBruijnGraph(reads):
	#Initialize a dictionary to hold the adjacency list.
	adjList = {}
	for read in reads:
		print "read",
		print read
		#Get the prefix and suffix:
		prefix = read[:-1]
		suffix = read[1:]
		print "pre,suf",
		print prefix,suffix
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
		print "KEYS",keyList
	valList = []
	for vals in adjList.values():
		for i in vals:
			valList.append(i)
		print "VALUES",valList
	for key in keyList:
		if key not in valList:
			first = key
			break
	adjList[""] = [first]
	#print adjList        
	return adjList

def balanceGraph(g):
	"""
	Add extra edges to g to make it "balanced"-- that is every
	node has the same incoming and outcoming edges.
	Will assume the g has a Hamiltonian path, so, only need to add in one edge.
	"""
	#Make a single list of the nodes with in-coming edges:
	allNeighborLists = g.values()
	allNeighbors = [i for nList in allNeighborLists for i in nList]
	#Find the node with no outgoing edges:
	for node in g.keys():
	#Find the node with no outgoing edges:
		if not g[node]:
			endNode = node
		#Find the node with no incoming edges:
		if g not in allNeighbors:
			begNode = node
	#Attach them
	g[endNode] = [begNode]

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
	#Add back to the dictionary if there's > 1 outgoing edges
	if len(value) > 1:
		unexplored[key] = value[1:]
	
	#While there are unexplored edges in graph:
	#for i in range(10):
	while unexplored:
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
				print i, cycle
				if cycle[i] in unexplored:
					neighbors = unexplored.pop(cycle[i])
					print "neighbors", neighbors
					if len(neighbors) > 1:
						#Put back the remaining unvisited edges:
						unexplored[cycle[-1]] = neighbors[1:]
					if len(neighbors) > 0:
						#Reorder cycle to put i at the end:
						cycle = cycle[:i] + cycle[i:] 
						#Add to cycle
						cycle.append(neighbors[0])
					break
	return cycle

def assemble(reads):
	"""
	Takes k_mers and returns a sequence
	"""
	g = createDeBruijnGraph(reads)
	print "The graph is: ", g     
	balanceGraph2(g)
	print "The balanced graph is: ", g
	
	print "\n\nBuilding up the Eulerian cycle"
	c = eulerianCycle(g)
	print "\n\nFound the cycle:", c
	#Missing step:  convert the cycle c into the sequence:

	#convert the cycle c into the sequence:
	sequence = ""

	for i in range(1,len(c)):
		klen= len(c[i])
		first = c[i-1]
		second = c[i]
		print first,second,"pairs"
		if first[1] == second[0]:
			print first,second[-1],"laps"
			#print "match"
			if sequence == "":
				sequence = sequence + str(first)+str(second[-1])
			else:
				sequence = sequence + str(second[-1])
		else:
			print "error"
			print "the kmer sequences do not overlap",
			print first,second,sequence
			sequence = sequence + "//"+str(second)
	print "\nThe raw sequence is: ",sequence
	seqlen = len(sequence)
	if sequence[0:klen] == sequence[(seqlen-klen):]:
		print "found overlap, new = ",
		sequence = sequence[0:seqlen-klen]
		print sequence
		if "//" in sequence:
			print "has break"
			loc = sequence.index("//")
			print loc,"start break",sequence[loc:loc+2]
			sequence =  sequence[loc+2:]+sequence[:loc]
			print "seq",sequence
	else:
		print "no overlaps"
		print "The final sequence is: ",sequence
	return sequence

def Composition(k,text):
	kmers = []
	for i in range(len(text)-k+1):
		#print i,text[i:i+k]
		kmers.append(text[i:i+k])
		kmers.sort()
	return kmers

if __name__ == "__main__":
	#infileString = "C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/textbookReads.txt"
	#reads = getReadsFromFile(infileString)
	#assemble(reads)

	#print "the kmers are:",Composition(3,"TATGGGGTGC")

	#newReads = Composition(5,"ACCGAAGCT")
	newReads = ["ACCGA","CCGAA","CGAAG","GAAGC","AAGCT"]
	#print newReads

	print assemble(newReads)

