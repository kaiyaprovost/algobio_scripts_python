def manhattan():
	import numpy as np

	east = np.array([[3,2,4,0],[3,2,4,2],[0,7,3,4],[3,3,0,2],[1,3,2,2]] )
	south = np.array([[1,0,2,4,3],[4,6,5,2,1],[4,4,5,2,1],[5,6,8,5,3]] )
	print east
	print south

	size = 5
	best = np.zeros((size,size))
	best[0,0] = 0
	
	traceback = np.zeros((size,size))
	UP = 1
	LEFT = -1

	for i in range(1,size):
		best[0,i] = best[0,i-1] + east[0,i-1]
		best[i,0] = best[i-1,0] + south[i-1,0]
		traceback[i,0] = UP
		traceback[0,i] = LEFT
		for j in range(1,size):
			#best[i,j] = max(best[i,j-1] + east[i,j-1],best[i-1,j] + south[i-1,j])
			if best[i,j-1]+east[i,j-1] > best[i-1,j]+south[i-1,j]:
				best[i,j] = best[i,j-1] + east[i,j-1]
				traceback[i,j] = LEFT
			else:
				best[i,j] = best[i-1,j] + south[i-1,j]
				traceback[i,j] = UP
			
	print best
	print traceback

	path = ""
	i = size-1
	j = size-1
	while i>0 or j>0:
		if traceback[i,j] == UP:
			path = "south "+path
			i -= 1
		else:
			path = "east "+path
			j -= 1
	print path

def sigma(x,y):
	if x == y:
		return 1
	else:
		return -1

def globAlign():
	import numpy as np

	seq1 = "TATATAGG"
	seq2 = "TAGAG"

	size1 = len(seq1)+1
	size2 = len(seq2)+1

	best = np.zeros((size1,size2))
	traceback = np.zeros((size1,size2))
	

	UP = 1
	LEFT = -1
	DIAG = 2

	delta = 1

	best[0,0] = 0
	for i in range(1,size1):
		best[i,0] = best[i-1,0] - delta
		traceback[i,0] = UP
	for i in range(1,size2):
		best[0,i] = best[0,i-1] - delta
		traceback[0,i] = LEFT
	for i in range (1,size1):
		for j in range(1,size2):
			best[i,j] = max(best[i,j-1]-delta,\
					best[i-1,j]-delta,\
					best[i-1,j-1]+sigma(seq1[i-1],seq2[j-1]))
			if best[i,j] == best[i-1,j-1]+sigma(seq1[i-1],seq2[j-1]):
				traceback[i,j] = DIAG
			elif best[i,j] == best[i-1,j]-delta:
				traceback[i,j] = UP
			else:
				traceback[i,j] = LEFT
		
	print best
	print traceback

	path1 = ""
	path2 = ""
	i = size1-1
	j = size2-1
	while i>0 or j>0:
		if traceback[i,j] == UP:
			path1 = seq1[i-1]+path1
			path2 = "-"+path2
			i = i-1
		elif traceback[i,j] == LEFT:
			path1 = "-"+path1
			path2 = seq2[j-1]+path2
			j = j-1
		else:
			path1 = seq1[i-1]+path1
			path2 = seq2[j-1]+path2
			j -= 1
			i -= 1
	print "an alignment is: "
	print path1
	print path2

def smithWater():
	import numpy as np

	seq1 = "GCGCAATG"
	seq2 = "GCCCTAGCG"

	size1 = len(seq1)+1
	size2 = len(seq2)+1

	best = np.zeros((size1,size2))
	traceback = np.zeros((size1,size2))

	UP = 1
	LEFT = -1
	DIAG = 2
	NULL = 0

	#delta = 1
	delta = 2

	best[0,0] = 0
	for i in range(1,size1):
		best[i,0] = 0
		traceback[i,0] = NULL
	for i in range(1,size2):
		best[0,i] = 0
		traceback[0,i] = NULL
	for i in range (1,size1):
		for j in range(1,size2):
			best[i,j] = max(best[i,j-1]-delta,\
					best[i-1,j]-delta,\
					best[i-1,j-1]+sigma(seq1[i-1],seq2[j-1]),\
					0)
			if best[i,j] != 0:
				if best[i,j] == best[i-1,j-1]+sigma(seq1[i-1],seq2[j-1]):
					traceback[i,j] = DIAG
				elif best[i,j] == best[i-1,j]-delta:
					traceback[i,j] = UP
				elif best[i,j] == best[i,j-1]-delta:
					traceback[i,j] = LEFT
				else:
					traceback[i,j] = NULL
			else:
				traceback[i,j] = NULL
			#diagdifs[i,j] = best[i,j] - best[i-1,j-1]
					
				
	print "best\n",best,"\n"
	print "trace\n",traceback,"\n"

	## use the trace, start at the bottom right corner
	## search the three around it
	## if there is a non-zero number, take that path
	## otherwise take the diagonal path and stop
	## output that 

	doneDict = {}
	todo = []
	temploc1 = ""
	temploc2 = ""
	local1 = []
	local2 = []

	i = size1-1
	j = size2-1

	while i > 0 and j > 0:
		node = str(i)+"-"+str(j)
		if traceback[i,j] == NULL:
			if temploc1 != "" and temploc2 != "":
				local1.append(temploc1)
				local2.append(temploc2)
				temploc1 = ""
				temploc2 = ""
			doneDict[node] = True
			if str(i-1)+"-"+str(j) not in doneDict:
				i = i - 1
			elif str(i)+"-"+str(j) not in doneDict:
				j = j - 1
			elif str(i-1)+"-"+str(j) not in doneDict:
				i = i - 1
				j = j - 1
			else:
				print "DEAD END"
		elif traceback[i-1,j-1] != NULL:
			if temploc1 == "" and temploc2 == "":
				temploc1 = str(best[i,j])+": "+seq1[i-1]
				temploc2 = str(best[i,j])+": "+seq2[i-1]
			#else:

if __name__ == "__main__":
	#manhattan()
	print "-------------------------------------------STOP1"
	globAlign()
	print "-------------------------------------------STOP2"
	smithWater()
