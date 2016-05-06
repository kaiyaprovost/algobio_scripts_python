from Bio import Entrez

Entrez.email = "klp2143@columbia.edu"

#handle = Entrez.einfo()
#record = Entrez.read(handle)
#print record["DbList"] ## all DB that can be queried

#handle = Entrez.einfo(db="pubmed")
#record = Entrez.read(handle)
#print record["DbInfo"]["Description"]		#Description of the database
#print record["DbInfo"]["Count"]			#Number of entries in pubmed

##handle = Entrez.einfo(db="nucleotide")
##record = Entrez.read(handle)
##print record["DbInfo"]["Description"]
##print record["DbInfo"]["Count"]	
##
##handle = Entrez.einfo(db="snp")
##record = Entrez.read(handle)
##print record["DbInfo"]["Description"]
##print record["DbInfo"]["Count"]	

##handle = Entrez.esearch(db="pubmed", term="biopython")
##record = Entrez.read(handle)
##print record["IdList"]
##
###What entries contain "AMNH"? 
##handle = Entrez.esearch(db="pubmed", term="AMNH")
##record = Entrez.read(handle)
##print record["IdList"]

##handle = Entrez.efetch(db="pubmed", id="21210977")
##print handle.read()

## first AMNH entry
##handle = Entrez.esearch(db="pubmed", term="AMNH")
##record = Entrez.read(handle)
##print min(record["IdList"])
##handle = Entrez.efetch(db="pubmed", id=min(record["IdList"]))
##print handle.read()

#handle = Entrez.esearch(db="nucleotide",term="Cypripedioideae[Orgn] AND matK[Gene]")
#record = Entrez.read(handle)
#print record["Count"] ## number of entries for the matK gene in Cypripedioideae. 

##handle = Entrez.esearch(db="nucleotide",term="Cardinalis[Orgn] AND ND2[Gene]")
##record = Entrez.read(handle)
##print record["Count"]

from Bio import SeqIO
##handle = Entrez.efetch(db="nucleotide", id="186972394",rettype="gb", retmode="text")
##for record in SeqIO.parse(handle, "genbank"):
##    print "Genbank id:\t", record.id
##    print "Sequence:\t", record.seq
##    print "Entry length:\t", len(record)
##handle.close()

##short_sequences = []
##for record in SeqIO.parse(open("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/cor6_6.gb","rU"),"genbank"):
##    if len(record.seq) < 300:
##        short_sequences.append(record)
##
##print "found {0} short sequences".format(len(short_sequences))
##output_handle = open("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/short_seqs.fasta","w")
##SeqIO.write(short_sequences,output_handle,"fasta")
##output_handle.close()

## CHALLENGES
##cardND2 = []
##countNum = 50
##count = 0
##handle = Entrez.esearch(db="nucleotide",term="Cardinalis[Orgn] AND ND2[Gene]")
##record = Entrez.read(handle)
##for i in (record["IdList"]):
##    handle = Entrez.efetch(db="nucleotide",id=i,rettype="gb",retmode="text")
##    for record in SeqIO.parse(handle,"genbank"):
##        #print record
##        #while count < countNum:
##        if len(record.seq) <= 1041:                
##            #print record
##            #print cardND2
##            cardND2.append(record)
##            count += 1
##            print count,
##print
##print "retrieved {0} card ND2 seqs".format(count)
##cardSeqsOut = open("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/cardSeqs.fasta","w")
##SeqIO.write(cardND2,cardSeqsOut,"fasta")
##cardSeqsOut.close()
##handle.close()

from lab8 import translate
from GC_content_type2 import getChunks

cardSeqsIn = open("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/cardSeqs.fasta","rU")
lines = cardSeqsIn.readlines()
cardSeqsIn.close()

outfile = open("C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/cardProts.fasta","w")

entries = getChunks(lines)
locusTemp = ""
for i in range(entries):
    for j in range(len(lines)):
        if lines[j][0] == ">":
            if j != 0:
                prot = translate(locusTemp)
                print >>outfile, prot
                locusTemp = ""
        elif lines[j][0] != ">":
            locusTemp += lines[j].strip()
        else:
            prot = translate(locusTemp)
            print >>outfile, prot          

outfile.close()














