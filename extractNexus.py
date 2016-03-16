import re

print "Welcome to newick tree-grabber! "
inName = str(input("path of the newick file: "))
## "C:/Users/Kaiya/Desktop/scratch_rosalind.txt"

infile = open(inName, "r")
fullfile = infile.read()

trees = re.findall("TREE\s(.+);",fullfile)

print "Your trees are: "
for i in range(len(trees)):
    print trees[i]

infile.close()


