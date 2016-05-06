
def readAdjList(infileString):
	infile = open(infileString,"rU")
	rawRead = infile.read().strip()
	infile.close()
	lines = rawRead.split("\n")
	adjDict = {}
	for line in lines:
		key = line.split(" -> ")[0]
		valueTemp = line.split(" -> ")[1:]
		value = "".join(valueTemp)
		adjDict[key] = value.split(",")
	return adjDict

def eulerianCycle2(graph): ## NOT RIGHT
	unexplored = graph.copy()
	key,value = unexplored.popitem()
	#print "key",key,"val",value
	cycle = [key,value[0]]
	#print cycle
	cycList = []
	if len(value) > 1:
		unexplored[key] = value[1:]

	#for i in range(20):
	while len(unexplored) != 0:
		if cycle == []:
			key,value = unexplored.popitem()
			cycle = [key,value[0]]
		#print "un" #,unexplored
		#print "cyc",len(unexplored),cycle
		#print "list",cycList
		if cycle[-1] in unexplored:
			neighbors = unexplored.pop(cycle[-1])
			if len(neighbors) > 0:
				if len(neighbors) > 1:
					unexplored[cycle[-1]] = neighbors[1:]
				cycle.append(neighbors[0])
		else:
			if cycle[-1] != cycle[0]:
				cycle.append(cycle[0])
			cycList.append(cycle)
			tempCycle = cycle[:]
			cycle = [] ##
			for i in range(len(tempCycle)):
				if tempCycle[i] in unexplored:
					#print "yup"
					neighbors = unexplored.pop(tempCycle[i])
					#print "\t",neighbors,neighbors[0]
					if len(neighbors) > 1:
						#print tempCycle[i],"TEMPT"
						unexplored[tempCycle[i]] = neighbors[1:]
						#print "back"
					if len(neighbors) > 0:
						#print neighbors,"ne"
						cycle.append(neighbors[0])
						#print "newcyc"
						#print cycle
					#else:
						#print "ERR"
					break
				#else:
					#print "wut"
	if cycList == []:
		cycList.append(cycle)
	#print cycle
	## TEST BEFORE DO CHECK TO SEE IF CYCLE BLANK
	if cycle != []:
		if cycle[-1] != cycle[0]:               ## IndexError: list index out of range
			cycle.append(cycle[0])
	else:
		print "CHECK"#cycList,"CHECK"
	if cycList[-1] != cycle:
		cycList.append(cycle)
	
	return cycList
##
##def getIntersectionList(cycList):
##    print "starting"
##    interList = []
##    for i in range(len(cycList)):
##        for j in range(len(cycList)):
##            if i < j:
##                setI = set(cycList[i])
##                setJ = set(cycList[j])
##                print "sets",setI,setJ
##                inter = setI.intersection(setJ)
##                print "inter",inter
##                if len(inter) != 0:
##                    interList.append((i,j))
##                    return interList

def getSingleIntersection(cycList):
	for i in range(len(cycList)):
		for j in range(len(cycList)):
			if i < j:
				#print "i,j,",i,j
				setI = set(cycList[i])
				setJ = set(cycList[j])
				#print setI,setJ
				inter = setI.intersection(setJ)
				if len(inter) != 0:
					#print "match",inter
					return (i,j)
	return ("NONE","NONE")

def linkCycles(cycList):
	if len(cycList) == 1:
		return cycList[0]
	copy = cycList[:]
	while len(copy) >= -1:
		key1,key2 = getSingleIntersection(copy)
		if key1 == "NONE":
			print "ACK" 
			print copy
			return ""
		#print key1,key2
		cyc1 = copy[key1] ## first one to try and link
		cyc2 = copy[key2] ## second one to try and link
		if key1 > key2:
			del copy[key1]
			del copy[key2]
		elif key2 > key1:
			del copy[key2]
			del copy[key1]
		#print "cycs",cyc1,cyc2,cyc1 in copy,cyc2 in copy
		#print "cycs",
		set1 = set(cyc1)
		set2 = set(cyc2)
		#print "sets",set1,set2
		inter = set1.intersection(set2) ## matching numbers between cycles
		#if swapCount > len(copy):
			#print "ERROR"
			#return "TOO LONG"
		if len(inter) == 0: ## if no matching numbers found
			#print "no overlap"
			if len(copy) == 0: ## if there are no more lists remaining
				return "No Eulerian Cycle Found"
##            if check == len(copy):
##                ## if you've checked the first list with all of the rest of them 
##                ## put the first list on the end of the list and start over
##                copy = copy[1:]+copy[0:1]
					
		else:
			#print "inter",inter
			intList = list(inter) ## for each intersection found
			connect = str(intList[0])
			#print "connnect",connect
			ind1 = cyc1.index(connect)
			ind2 = cyc2.index(connect)
			#print "indexes",ind1,ind2
			reorder1 = cyc1[ind1:-1]+cyc1[:ind1+1]
			## makes it so that the intersection is the start/end of cycle
			reorder2 = cyc2[ind2:-1]+cyc2[:ind2+1]
			#print "reorders",reorder1,reorder2
			if reorder1[-1]==reorder2[0]:
				#print "match"
				concatCyc = reorder1[:-1]+reorder2
				#print "concat",concatCyc
				## links them together at the intersection
				if len(copy) == 0:
					#print "return"
					return concatCyc
				else:
					#print "change"
					copy.append(concatCyc)
					#print cyc3
					#copy = cyc3
					continue
			else:
				return "ERROR"
						

if __name__ == "__main__":
	infileString = "C:/Users/Kaiya/Desktop/rosalind_scratch.txt"
	adjDict = readAdjList(infileString)
	#print adjDict
	cycList = eulerianCycle2(adjDict)
	#print cycList

	#print "test"
	interList = getSingleIntersection(cycList)
	#print interList

	print len(cycList)
				
						   


	
	print "-------------"
	x = linkCycles(cycList)
	print x == ""
	print x == "TOO LONG"
	print x == "ERROR"
	print x == "No Eulerian Cycle Found"

	outfile = open("C:/Users/Kaiya/Desktop/rosalind_scratch_ans.txt","w")

	string = "->".join(x)
	print >>outfile, string

	outfile.close()
