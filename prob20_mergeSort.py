files = open("C:/Users/Kaiya/Desktop/rosalind_mer.txt","rU")
n = files.readline()
a = files.readline()
m = files.readline()
b = files.readline()

files.close()

n = int(n.strip())
a = a.split()
a = [int(x) for x in a]
m = int(m.strip())
b = b.split()
b = [int(y) for y in b]

outfile = open("C:/Users/Kaiya/Desktop/rosalind_mer_ans.txt","w")

def merge(a,b,n,m,outfile):
    out = []
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < b[j]:
            print >>outfile, a[i],
            i += 1
        else:
            print >>outfile, b[j],
            j += 1
    if i < n:
        for k in a[i:]:
            print >>outfile, k,
    if j < m:
        for h in b[j:]:
            print >>outfile, h,

merge(a,b,n,m,outfile)

outfile.close()
