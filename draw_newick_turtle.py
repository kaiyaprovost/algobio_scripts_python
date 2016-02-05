import turtle

## raw string
## "((Sau, (Cer, (Car, (Orn, Man)))), (Leso,(Thy, (Eru, Mar))))"

## single letter string
phylo = "((S,(C,(R,(O,N)))),(L,(T,(E,M))))"

#phylo = "(A,(B,C))"

#phylo = "(A,B,C)"

raph = turtle.Turtle()
raph.speed(1)
raph.pensize(3)
raph.shape("turtle")

wn = turtle.Screen()
wn.bgcolor("lightgreen")

colBranch = 0
lenBranch = 1

icount = 0
commaCount = 1

colors = ["black","red","blue","orange","purple","brown","hotpink"]

maxLen = 0

head = 135
raph.setheading(head)
raph.color(colors[colBranch])
for i in phylo:
    icount = icount + 1
    if i == "(":
        ## move up to next colBranch
        colBranch = colBranch + 1
        raph.color(colors[colBranch])
        raph.forward(100/lenBranch)
        raph.setheading(head)
    if i == ")":
        ## move back a colBranch
        colBranch = colBranch - 1
        raph.color(colors[colBranch])
        raph.penup()
        raph.left(90)
        lenBranch = lenBranch - 1
        if lenBranch > maxLen:
            maxLen = lenBranch
        raph.forward(100/lenBranch)
        raph.pendown()
        raph.setheading(head)
    if i == ",":
        ## stay same color
        ## check for polytomy
        if phylo[icount-2] == ",":
            print "polytomy"
        raph.left(180)
        raph.penup()
        raph.forward(100/lenBranch)
        raph.pendown()
        raph.left(90)
        raph.forward(100/lenBranch)
        #raph.stamp()
        raph.setheading(head)
        lenBranch = lenBranch + 1
        if colBranch > maxLen:
            maxLen = colBranch
    if i not in ["(", ")", ","]:
        raph.write(i)

#print maxLen    
    
wn.exitonclick()
