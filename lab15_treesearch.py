def buildRandomTree(seqList):
	import random
	## put all leaves in dict
	adjList = {}
	## make parentless todo list
	orphans = []
	for (key,value) in seqList:
		adjList[key] = ["",value,[]]
	orphans = adjList.keys()
	## while len(parentless) > 2
	count = 0
	while len(orphans) > 2:
		## choose 2 kids and remove
		count += 1
		newName = "in"+str(count)
		first = random.choice(orphans)
		orphans.remove(first)
		second = random.choice(orphans)
		orphans.remove(second)

		## make node and kids
		adjList[newName] = ["","",[first,second]]
		adjList[first][0] = newName
		adjList[second][0] = newName

		## add parent to parentless
		orphans.append(newName)

	## when last 2 parentless, make root
	adjList["root"] = ["","",[orphans[0],orphans[1]]]
	adjList[orphans[0]][0] = "root"
	adjList[orphans[1]][0] = "root"
	
	return adjList

def convertNewick(treeDict,node):
	## if node is leaf of tree
	#print "TEST"
	#print treeDict["in7"]
	if treeDict[node][2] == []:
		return node
	else:
		kid1 = treeDict[node][2][0]
		kid2 = treeDict[node][2][1]
		left = convertNewick(treeDict,kid1)
		#print left
		right = convertNewick(treeDict,kid2)
		#print right
		string = "("+left+","+right+")"
		return string	



"""
Takes a tree stored as dictionary and an internal node 
in the tree, and
Returns the two NNI neighbors of the tree around that node.
"""
def nniNeighbor(t, node):
	import copy
	if node != "root":
		if len(t[node][2]) != 0:
			#Let sib be the sibling of node.
			p = t[node][0]
			sibs = copy.deepcopy(t[p][2])
			sibs.remove(node)
			sib = sibs[0]
			#Let kid1, kid2 be the children of node.
			kid1 = t[node][2][0]
			kid2 = t[node][2][1]
			#Make two (deep) copies of t: tree1 and tree2.
			tree1 = copy.deepcopy(t)
			tree2 = copy.deepcopy(t)
			#Switch sib and kid1 in tree1.
			tree1[p][2] = [node,kid1]   #Set p's kids to be node and kid1
			tree1[kid1][0] = p          #Set kid1's parent to be p
			tree1[node][2] = [sib,kid2]    #Set n's kids to be sib and kid2
			tree1[sib][0] = node        #Set sib's parent to be node
			#Switch sib and kid2 in tree2.
			tree2[p][2] = [node,kid2]   #Set p's kids to be node and kid1
			tree2[kid2][0] = p          #Set kid1's parent to be p
			tree2[node][2] = [sib,kid1]    #Set n's kids to be sib and kid2
			tree2[sib][0] = node        #Set sib's parent to be node           
			#Return tree1 and tree2.
			return (tree1,tree2)
	    
	    
def maxNeighbor(t0):
	import copy
	import parsimonyScore as ps
	toDo = copy.deepcopy(t0["root"][2])     #Start the to do list with the kids of root.
	bestTree = t0  #Use the inputs as the best tree and best score.
	bestScore = ps.scoreTree(t0)

	print "Neighbors:"
	while len(toDo) > 0:
		nextNode = toDo.pop()
		toDo.extend(copy.deepcopy(t0[nextNode][2]))
		if len(t0[nextNode][2]) > 0: 
			t1, t2 = nniNeighbor(t0,nextNode)
			s1 = ps.scoreTree(t1)
			s2 = ps.scoreTree(t2)            
			print "\t", convertNewick(t1, "root"), s1
			print "\t", convertNewick(t2, "root"), s2
			if s1 < bestScore and bestTree != t1:
				#print s1, bestScore
				bestTree = t1
				bestScore = s1
			if s2 < bestScore and bestTree != t2:
				#print s2, bestScore
				bestTree = t2
				bestScore = s2
			if s1 == bestScore and bestTree != t1:
				#print s1, bestScore,"E"
				bestTree = t1
				bestScore = s1
			if s2 == bestScore and bestTree != t2:
				#print s2, bestScore,"E"
				bestTree = t2
				bestScore = s2

	return bestTree, bestScore

def treeSample(sequences):
	import parsimonyScore as ps
	steps = 0
	bestTree = buildRandomTree(sequences)
	bestScore = ps.scoreTree(bestTree)
	for iteration in range(1000):
		## choose random tree
		newTree = buildRandomTree(sequences)
		## score the tree
		newScore = ps.scoreTree(newTree)
		#print convertNewick(newTree,"root")
		#print newScore
		if newScore < bestScore:
			bestScore = newScore
			bestTree = newTree
			steps += 1
	return steps,bestTree,bestScore

def treeSearch(sequences,bestTree,bestScore):
	import parsimonyScore as ps
	#bestTree = buildRandomTree(sequences)
	#bestScore = ps.scoreTree(bestTree)
	print "org tree\t",convertNewick(bestTree,"root"),bestScore
	#print bestScore,"SCORE"
	steps = 0
	for iteration in range(1000):
		#print iteration,"best", convertNewick(bestTree,"root"),bestScore
		## get the best NNI nbr
		nbrTree,nbrScore = maxNeighbor(bestTree)
		#print "  nrb ",convertNewick(nbrTree,"root"),nbrScore
		#nbrScore = ps.scoreTree(nbrTree)

		## if any have better score, choose to be current tree
		if nbrScore < bestScore:
			bestScore = nbrScore
			bestTree = nbrTree
			steps += 1
		elif nbrScore == bestScore:
			#break
			bestScore = nbrScore
			bestTree = nbrTree
##		## else stuck
		else:
			#print "break"
			break
	## print num steps, tree, and score
	return steps,bestTree,bestScore

##def treeSearch2(sequences):
##	import parsimonyScore as ps
##	#Choose randomly a tree to be bestSoFar.
##	bestSoFar = buildRandomTree(sequences)
##	#Score the tree, bestSoFar.
##	bestScore = ps.scoreTree(bestSoFar)
##	print "Start:\t", convertNewick(bestSoFar, "root"), bestScore
##	#For 1000 steps:
##	for i in range(1000):
##	#   Make a list of all the NNI neighbors of bestSoFar
##		neighborBest, neighborScore = maxNeighbor(bestSoFar)
##	#   if any of the NNI neighbors of bestSoFar have better score,
##		if neighborScore < bestScore:
##	#       choose it to be the current tree
##			bestSoFar = neighborBest
##			bestScore = neighborScore
##		
##		#print "Best so far:\t", convertNewick(bestSoFar, "root"), bestScore
##	return bestSoFar, bestScore

if __name__ == "__main__":
##	import parsimonyScore as ps
##	
##	
##	tree = {"ape": ["","",[]],
##		"baboon": ["","",[]],
##		"chimp":["","",[]],
##		"dog":["","",[]],
##		"elephant":["","",[]],
##		"fox":["","",[]]}
##
##	parentless = ["ape","baboon","chimp","elephant","fox","dog"]

	seqList = [("ape","A A A A A"),
		   ("baboon","A A A A G"),
		   ("chimp","C A A A A"),
		   ("dog","T G G G G"),
		   ("elephant","T G A C A"),
		   ("fox","A A G G C")]

##	bestTree,bestScore = treeSample(seqList)
##	print  "\nBest from sample:", convertNewick(bestTree,"root"),":", bestScore
##
##	steps,bestTree,bestScore = treeSearch(seqList)
##	print  "\nBest from sample:", convertNewick(bestTree,"root"),":", bestScore,"# steps",steps
##

##	rand = buildRandomTree(seqList)
##	
##	randNew = convertNewick(rand,"root")
##	print randNew
##
##	score = ps.scoreTree(rand)
##	print score

	flatSeq = [("boring1", "A A A A A A A A A A A A A A A A"),
		   ("boring2", "A A A A A A A A A A A A A A A A"),
		   ("boring3", "A A A A A A A A A A A A A A A A"),
		   ("boring4", "A A A A A A A A A A A A A A A A"),
		   ("boring5", "A A A A A A A A A A A A A A A A"),
		   ("boring6", "A A A A A A A A A A A A A A A A"),
		   ("boring7", "A A A A A A A A A A A A A A A A"),
		   ("boring8", "A A A A A A A A A A A A A A A A"),
		   ("boring9", "A A A A A A A A A A A A A A A A"),
		   ("boring10", "A A A A A A A A A A A A A A A A")]
	compSeq = [("1","0 0 0 0 0 0 0 0"),
		   ("2","0 0 0 0 0 0 0 0"),
		   ("3","1 0 0 0 0 0 0 0"),
		   ("4","1 1 0 0 0 0 0 0"),
		   ("5","1 1 1 0 0 0 0 0"),
		   ("6","1 1 0 1 0 0 0 0"),
		   ("7","1 1 0 1 1 0 0 0"),
		   ("8","1 1 0 1 1 1 0 0"),
		   ("9","1 1 0 1 1 1 1 0"),
		   ("10","1 1 0 1 1 1 1 1")]
	ruggedSeq = [("a", "A A A A A A A A A A A"),
		     ("b", "A T A T A T A T A T A"),
		     ("c", "C C T A A A A T A T A"),
		     ("d", "T A T A T A T A T A T"),
		     ("e", "C T A T A T G T G T A"),
		     ("f", "C C T A A G A T A T A"),
		     ("g", "G G G C T A T A T A T")]

	##((((7,8),((10,9),6)),(5,4)),(3,(1,2))), score 9
	##(((78,1096),54),312), score 9
	bestRandComp = {'10':  ['in2', '1 1 0 1 1 1 1 1', []],
			'in8':  ['root', '1 0 0 0 0 0 0 0', ['3', 'in5']],
			'in4':  ['in6', '1 1 0 1 1 0 0 0', ['in2', '6']],
			'in5':  ['in8', '0 0 0 0 0 0 0 0', ['1', '2']],
			'in6':  ['in7', '1 1 0 1 1 0 0 0', ['in3', 'in4']],
			'in7':  ['root', '1 1 0 0 0 0 0 0', ['in6', 'in1']],
			'in1':  ['in7', '1 1 0 0 0 0 0 0', ['5', '4']],
			'in2':  ['in4', '1 1 0 1 1 1 1 0', ['10', '9']],
			'in3':  ['in6', '1 1 0 1 1 0 0 0', ['7', '8']],
			'1':    ['in5', '0 0 0 0 0 0 0 0', []],
			'3':    ['in8', '1 0 0 0 0 0 0 0', []],
			'2':    ['in5', '0 0 0 0 0 0 0 0', []],
			'5':    ['in1', '1 1 1 0 0 0 0 0', []],
			'4':    ['in1', '1 1 0 0 0 0 0 0', []],
			'7':    ['in3', '1 1 0 1 1 0 0 0', []],
			'6':    ['in4', '1 1 0 1 0 0 0 0', []],
			'9':    ['in2', '1 1 0 1 1 1 1 0', []],
			'8':    ['in3', '1 1 0 1 1 1 0 0', []],
			'root': ['', '1 1 0 0 0 0 0 0', ['in7', 'in8']]}

	bestScoreComp = 9

	#print convertNewick(bestRandComp,"root"), "YA"
	
	steps,bestTree,bestScore = treeSearch(compSeq,bestRandComp,bestScoreComp)
	print  "\nBest from search:", convertNewick(bestTree,"root"),":", bestScore,"# steps",steps

##	print "test tree"
##	steps,bestTree,bestScore = treeSample(seqList)
##	print  "\nBest from sample:", convertNewick(bestTree,"root"),":", bestScore,", steps",steps
##	steps,bestTree,bestScore = treeSearch(seqList)
##	print  "\nBest from search:", convertNewick(bestTree,"root"),":", bestScore,"# steps",steps
##
##	
##	print "------------------------------------------\nflat tree"
##	steps,bestTree,bestScore = treeSample(flatSeq)
##	print  "\nBest from sample:", convertNewick(bestTree,"root"),":", bestScore,", steps",steps
##	steps,bestTree,bestScore = treeSearch(flatSeq)
##	print  "\nBest from search:", convertNewick(bestTree,"root"),":", bestScore,"# steps",steps
##
##	print "------------------------------------------\ncomp tree"
##	steps,bestTree,bestScore = treeSample(compSeq)
##	print  "\nBest from sample:", convertNewick(bestTree,"root"),":", bestScore,", steps",steps
##	steps,bestTree,bestScore = treeSearch(compSeq)
##	print  "\nBest from search:", convertNewick(bestTree,"root"),":", bestScore,"# steps",steps
##
##	print "------------------------------------------\nrugged tree"
##	steps,bestTree,bestScore = treeSample(ruggedSeq)
##	print  "\nBest from sample:", convertNewick(bestTree,"root"),":", bestScore,", steps",steps
##	steps,bestTree,bestScore = treeSearch(ruggedSeq)
##	print  "\nBest from search:", convertNewick(bestTree,"root"),":", bestScore,", steps",steps
	
##	print "------------------------------------------\ncomp tree2"
##	for i in range(10):
##		steps,bestTree,bestScore = treeSample(compSeq)
##		print  "Best from sample:", convertNewick(bestTree,"root"),":", bestScore,", steps",steps
##	print "\n\tSEARCHES\n"
##	for j in range(10):
##		steps,bestTree,bestScore = treeSearch(compSeq)
##		print  "\tBest from search:", convertNewick(bestTree,"root"),":", bestScore,"# steps",steps
##	for k in range(10):
##		bestTree,bestScore = treeSearch2(compSeq)
##		print  "\tBest from search:", convertNewick(bestTree,"root"),":", bestScore
##		print "-----"
		

##	prevScore = 100
##	prevTree = {}
##	for w in range(1000):
##		if w % 10 == 0:
##			print w,
##		steps,bestTree,bestScore = treeSample(compSeq)
##		if bestScore < prevScore:
##			prevScore = bestScore
##			prevTree = bestTree
##	print prevScore
##	print convertNewick(bestTree,"root")


	
