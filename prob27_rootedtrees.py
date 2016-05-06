import math

## num rooted trees:
## (2n - 3)!!
## =
## (2n - 3)! / (n-2)! * 2^(n-2)
## math.factorial(2n - 4)
## /
## math.factorial(n-2) * math.pow(2,(n-2))

n = int(input("number of leaves: "))

def rootTreeCalc(n):
    num = int(math.factorial(2*n - 3))
    den = int(math.factorial(n-2)) * int(math.pow(2,(n-2)))
    root = num/den
    return root

print rootTreeCalc(n) % 1000000
print "---"

##for n in range(2,18):
##    ans = rootTreeCalc(n) % 1000000
##    print ans
