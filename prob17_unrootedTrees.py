import math

## num unrooted trees:
## (2n - 5)!!
## (2n - 4)! / (n-2)! * 2^(n-2)
## math.factorial(2n - 4)
## /
## math.factorial(n-2) * math.pow(2,(n-2))

n = int(input("number of leaves: "))

def unrootTreeCalc(n):
    num = int(math.factorial(2*n - 4))
    den = int(math.factorial(n-2)) * int(math.pow(2,(n-2)))
    unroot = num/den
    return unroot

ans = unrootTreeCalc(n) % 1000000

print ans
print "----------"

for i in range(2,18):
    ans = unrootTreeCalc(i) % 1000000
    print ans
