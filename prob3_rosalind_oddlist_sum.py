## input a and b
a = int(input("Value of A")) 
b = int(input("Value of B"))

## create lists to populate
oddlist = [] ## odd list is list of odd numbers between a and b inclusive
evenlist = [] ## even list is list of even numbers between a and b inclusive

## for numbers between a and b, inclusive:
for i in range(a,(b+1)):
    #print(i) ## for testing
    #print(i % 2) ## for testing
    if i % 2 == 0:
        ## if number is even, remainder after dividing by 2 is zero
        ## do not sum
        evenlist.append(i) ## add to even list
    if i % 2 == 1:
        ## if number is odd, remainder after dividing by 2 is one
        ## sum
        oddlist.append(i) ## add to odd list

#print(oddlist) ## for testing
print(sum(oddlist)) ## print the summary of the odd numbers
