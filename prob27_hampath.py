##def getDAGSFromFile(infile):
##	f = open(infile)
##	#Depending on the file, could have extra newlines at end, strip off:
##	data = f.read().rstrip()
##	return data.split("\n\n")
##
##def getDAGSFromList(dagList):
##	splitDags = []
##	for dag in dagList:
##		tempDag = dag.split("\n")
##		splitDags.append(tempDag)
##	return splitDags
		

def readHamDag(infile):
	f = open(infile,"rU")
	data = f.read().strip()
	lines = data.split("\n")
	return lines

def splitDags(lines):
	labelLine = 1
	dagList = []
	numDags = int(lines[0])
	for i in range(numDags):
		label = lines[labelLine].split()
		#print label
		rows = int(label[1])
		tempDag = lines[labelLine:labelLine+rows+1] ## includes the label line
		dagList.append(tempDag)
		labelLine = labelLine + rows + 1
	return dagList					


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

def topSort2(adj):
	## find all parents
	## add to list
	## pick one parent
	## remove it
	## check if the kids are parents
	## if so add to list
	## repeat

	import copy
	adjacency = copy.deepcopy(adj)

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
		#print "parent",parent
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

def hamPath2(adj,sort):
	for key in range(len(sort)-1):
		if  sort[key+1] not in adj[sort[key]][1]:
			return -1
	out = ["1"]+[str(i) for i in sort]
	return " ".join(out)

##def hamPath(adj):
##	orphan = [] ## no parents
##	dink = [] # #no children
##	for key in adj:
##		if adj[key][0] == [None]:
##			#node has no parents
##			orphan.append(key)
##			if len(orphan) > 1:
##				# if more than one node has no parents, cannot be ham path 
##				#print "CANNOT BE HAM PATH"
##				return -1
##		if adj[key][1] == [None]:
##			#node has no children
##			dink.append(key)
##			if len(dink) > 1:
##				# if more than one node has no children, cannot be ham path
##				#print "CANNOT BE HAM PATH 2"
##				return -1
##
##	print "orphans",orphan
##	print "dinks",dink
##
##	if orphan == dink:
##		## if there are any abandoned nodes with no parents or children, cannot be ham path
##		#print "CANNOT BE HAM PATH 3"
##		return -1
##
##	#return 0
##
##	first = orphan[0]
##	last = dink[0]
##
##	kids = set(adj[first][1])
##	parents = set(adj[last][0])
	

def main():
	#print "hi"

	## CODE DOES NOT SPlIT LINES UP
	## NEED TO MANUALLY TELL IT

	infileString = "C:/Users/Kaiya/Desktop/rosalind_hdag.txt"
	readDags = readHamDag(infileString)
	dags = splitDags(readDags)

	numDags = dags[0]
	eachDags = dags[1:]

##	splits = getDAGSFromList(eachDags)

	outfile = open("C:/Users/Kaiya/Desktop/rosalind_hdag_ans.txt","w")
		
	for rawDag in dags:
		dagNum = rawDag[0]
		onlyDag = rawDag[1:]
		adjDict = adjList(onlyDag)
		
		sort =  topSort2(adjDict)
		
		output =  hamPath2(adjDict,sort)
		#print output
		print >>outfile, output

	outfile.close()

if __name__ == "__main__":
	main()
