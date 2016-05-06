dna = str(input("dna strand as string"))

comp = ""
for bp in range(1,(len(dna)+1)):
    if dna[-bp] == "A":
        comp = comp + "T"
    elif dna[-bp] == "T":
        comp = comp + "A"
    elif dna[-bp] == "G":
        comp = comp + "C"
    elif dna[-bp] == "C":
        comp = comp + "G"
    else: 
        comp = comp + dna[-bp]
print(comp)
