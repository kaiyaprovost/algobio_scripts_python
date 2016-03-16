files = open("C:/Users/Kaiya/Desktop/rosalind_ba1h.txt","rU")
patt = files.readline()
text = files.readline()
mism = files.readline()
patt = patt.strip()
text = text.strip()
mism = int(mism.strip())
#print patt
#print text
print mism
files.close()
outfile = open("C:/Users/Kaiya/Desktop/rosalind_ba1h_ans.txt","w")
match = []
for i in range(len(patt),len(text)+1):
    mut = 0
    temp = text[i-len(patt):i]
    for j in range(len(temp)):
        if temp[j] != patt[j]:
            mut += 1
    if mut <= mism:
        match.append((i-len(patt)))
        print >>outfile, i-len(patt),
                          
#print match
outfile.close()
