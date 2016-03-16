## less than 100 genbanks at at time on their preferred server



##

##from Bio import Entrez

##Entrez.email = "klp2143@columbia.edu"
##
##handle = Entrez.einfo()
##
##record = Entrez.read(handle)
##record["DbList"]

##from Bio import SeqIO
##shortSeq = []
##for record in SeqIO.parse(open("cor6_6.gb","rU"),"genbank"): ## there is no such file currently
##    if len(record.seq) < 300:
##        shortSeq.append(record)
##print "Found {0} short sequences".format(len(shortSeq))
##
##outputHandle = open("shortSeqs.fasta","w")
##SeqIO.write(shortSeq,outputHandle,"fasta")
##outputHandle.close()



def translate(dna):
    gencode = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
           'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
           'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
           'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
           'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
           'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
           'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
           'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
           'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
           'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
           'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
           'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
           'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

    prot = ""
    for bp in range(0,len(dna),3):
        codon = dna[bp:bp+3]
        if len(codon) == 3:
            prot = prot + gencode.get(codon)
    return prot

dna = "GATGGAACTTGACTACGTAAATT"

print translate(dna)

def bpCounts(dna): ## works as is for DNA, RNA, or PROTEIN
    bpCounts = {}
    for bp in dna:
        if bp in bpCounts:
            bpCounts[bp] += 1
        else:
            bpCounts[bp] = 1
    return bpCounts

print bpCounts(dna)

prot = "IMTN"

##def translateMany(data,dataType):
##    gencode = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
##           'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
##           'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
##           'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
##           'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
##           'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
##           'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
##           'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
##           'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
##           'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
##           'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
##           'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
##           'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
##
##    out = ""
##    
##    if dataType != "PROTEIN":
##        if dataType == "RNA":
##            rna = data.replace("T","U")
##            out = translate(rna)
##        else:
##            out = translate(data)
##    else:
##        
##
##    return out



