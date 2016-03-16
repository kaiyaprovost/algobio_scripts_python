## return even numbered lines of file

infile = open("C:/Users/Kaiya/Desktop/rosalind_ini5.txt","r")

outfile = open("C:/Users/Kaiya/Desktop/rosalind_ini5_out.txt","w")

lines = infile.readlines()
for i in range(len(lines)):
    if (i+1) % 2 == 0:
        print >>outfile, lines[i],

infile.close()
outfile.close()
