def newLabel(lab1,lab2):
	'''
	Takes two labels and reutrns the label of their parent
	'''
	base1 = lab1.split(" ")
	base2 = lab2.split(" ")
	newLab = []

	for i in range(len(base1)):
		if base1[i] == base2[i]:
			newLab.append(base1[i])
		else:
			set1 = set(base1[i])
			set2 = set(base2[i])
			print "set1:",set1
			print "set2:",set2
			inter = set1.intersection(set2)
			if len(inter) == 0:
				union = set1.union(set2)
				newLab.append("".join(union))
			else:
				newLab.append("".join(inter))
				
	return " ".join(newLab)

def firstPass(t,n):
	'''
	Labels all internal nodes of the tree from the leaves
	'''
	## assumes all leaves have labels
	## check if node has label
	if t[n][1] != "":
		return t[n][1]
	else:
		## if not, get the label from children
		## assumes binary
		kid1 = t[n][2][0]
		kid2 = t[n][2][1]
		newLab = newLabel(firstPass(t,kid1),firstPass(t,kid2))
		t[n][1] = newLab
		return newLab

def forceLabels(t,labels,kid):
	'''
	Forces an ambiguous label to one particular non-ambiguous version
	'''
	count = 0
	kLabels = t[kid][1].split(" ")
	#print labels,kLabels
	if labels == kLabels:
		#print "\tWHOLE MATCH"
		return 0
	for i in range(len(labels)):
		if kLabels[i] != labels[i]:
			set1 = set(kLabels[i])
			set2 = set(labels[i])
			#print "\t",set1,set2
			inter = set1.intersection(set2)
			if len(inter) == 0:
				# no overlap, choose one
				#print "\t\tNO OVER"
				kLabels[i] = kLabels[i][:1]
				count = count + 1
			else:
				#do overlap, choose one to use as label
				#print "\t\tYES OVER"
				kLabels[i] = inter.pop()
		#else:
			#print "\tMATCH"
	t[kid][1] = " ".join(kLabels)
	return count
	

def secondPass(t,n):
	'''
	Makes all labels non-ambiguous
	'''
	# assumes all leaves have labels
	# check if there's a label for each
	score = 0
	labels = t[n][1].split(" ")
	if n == "root":
		for i in range(len(labels)):
			# for root, if more than one label, use just the first one
			labels[i] = labels[i][:1]
		t[n][1] = " ".join(labels)
	if len(t[n][2]) > 0:
		# there are children, not a leaf
		# assumes binary tree
		kid1 = t[n][2][0]
		kid2 = t[n][2][1]
		# force the labels for the kids
		int1 = forceLabels(t,labels,kid1)
		int2 = forceLabels(t,labels,kid2)
		score = int1 + int2
		print "mismatches between parent and kids:",n,kid1,int1,kid2,int2
		# repeat for the kids
		score = score + secondPass(t,kid1)
		score = score + secondPass(t,kid2)
	return score



def main():
	tree = {"root" : ["","",["i1","i2"]],
		"i1": ["root","", ["a", "i3"]],
		"i2": ["root","", ["b", "c"]],
		"i3": ["i1","", ["d","e"]],
		"a": ["i1","T A A A A", []],
		"b": ["i2","A A A A G", []],
		"c": ["i2","C A A A T", []],
		"d": ["i3","A A A A A", []],
		"e": ["i3","T A A A A", []]}

	tree2 = {"root" : ["","",["i1","i2"]],
		"i1": ["root","", ["d", "i3"]],
		"i2": ["root","", ["b", "c"]],
		"i3": ["i1","", ["a","e"]],
		"d": ["i1","T A A A A", []],
		"b": ["i2","A A A A G", []],
		"c": ["i2","C A A A T", []],
		"a": ["i3","A A A A A", []],
		"e": ["i3","T A A A A", []]}

	tree3 = {"root" : ["","",["c","i2"]],
		 "c": ["root","C A A A T", []],
		 "i2": ["root","", ["b", "i1"]],
		 "b": ["i2","A A A A G", []],
		"i1": ["i2","", ["d", "i3"]],
		"i3": ["i1","", ["a","e"]],
		"d": ["i1","T A A A A", []],
		"a": ["i3","A A A A A", []],
		"e": ["i3","T A A A A", []]}

	for i in tree3:
		print i,tree3[i]
	print "-----1"

	print newLabel(tree3["a"][1],tree3["b"][1])
	print "-----2"

	print firstPass(tree3,"root") ## labels all of the internal nodes
	print "-----3"

	for i in tree3:
		print i,tree3[i]
	print "-----4"

	treeScore = secondPass(tree3,"root")
	print "-----5"

	for i in tree3:
		print i,tree3[i]
	print "-----6"

	print "SCORE OF TREE:",treeScore
	print "-----7"

	
if __name__ == "__main__":
    main()
