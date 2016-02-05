var1 = str(input("dna string 1"))
var2 = str(input("dna string 2"))

mutCount = 0

for i in range(len(var1)):
    if var1[i] == var2[i]:
        print("match")
    else:
        print("no match")
        mutCount = mutCount + 1

print mutCount
