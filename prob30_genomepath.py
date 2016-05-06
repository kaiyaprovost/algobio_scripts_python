## copied dubruijn graphs file - in order, does not need cycle

def getReadsFromFile(infile):
	f = open(infile,"rU")
	#Depending on the file, could have extra newlines at end, strip off:
	data = f.read().rstrip()
	return data.split("\n")

def assemble(c):
	"""
	Takes k_mers and returns a sequence
	"""
	
	sequence = ""
	for i in range(1,len(c)):
		klen= len(c[i])
		first = c[i-1]
		second = c[i]
		#print first,second,"pairs"
		if first[1] == second[0]:
			#print first,second[-1],"laps"
			#print "match"
			if sequence == "":
				sequence = sequence + str(first)+str(second[-1])
			else:
				sequence = sequence + str(second[-1])
		else:
			#print "error"
			#print "the kmer sequences do not overlap",
			#print first,second,sequence
			sequence = sequence + "//"+str(second)
	#print "\nThe raw sequence is: ",sequence
	seqlen = len(sequence)
	if sequence[0:klen] == sequence[(seqlen-klen):]:
		#print "found overlap, new = ",
		sequence = sequence[0:seqlen-klen]
		#print sequence
		if "//" in sequence:
			#print "has break"
			loc = sequence.index("//")
			#print loc,"start break",sequence[loc:loc+2]
			sequence =  sequence[loc+2:]+sequence[:loc]
			#print "seq",sequence
	#else:
		#print "no overlaps"
		#print "The final sequence is: ",sequence
	return sequence

if __name__ == "__main__":
    infileString = "C:/Users/Kaiya/Desktop/rosalind_ba3b.txt"
    reads = getReadsFromFile(infileString)
    #print reads
    seq = assemble(reads)

    outfile = open("C:/Users/Kaiya/Desktop/rosalind_ba3b_ans.txt","w")

    #print seq
    print >>outfile, seq

    outfile.close()

##    count = 0
##    for i in range(len(should)):
##        if should[i] != seq[i]:
##            print i,"NO MATCH",should[i],seq[i]
##            count = count +1

    #print should == seq
