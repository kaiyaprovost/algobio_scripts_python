## copied composition file

def Composition(k,text):
	kmers = []
	for i in range(len(text)-k+1):
		#print i,text[i:i+k]
		kmers.append(text[i:i+k])
		kmers.sort()
	return kmers

if __name__ == "__main__":
    infileString = "C:/Users/Kaiya/Desktop/rosalind_ba3a.txt"
    infile = open(infileString,"rU")
    k = infile.readline()
    text = infile.readline()
    infile.close()

    k = int(k.strip())
    text = text.strip()

    kmers = Composition(k,text)

    outfile = open("C:/Users/Kaiya/Desktop/rosalind_ba3a_ans.txt","w")
    
    for i in kmers:
        print >>outfile, i

    outfile.close()
