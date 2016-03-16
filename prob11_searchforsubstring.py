full = str(input("full string "))
motif = str(input("motif "))

## wants 1 based numbers

counti = 1

for i in range(len(full)):
    if full[i:i+len(motif)] == motif:
        print counti,
    counti = counti + 1 
