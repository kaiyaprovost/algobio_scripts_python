import turtle

## set up turtle and screen

raph = turtle.Turtle()
wn = turtle.Screen()

raph.color("red")
wn.bgcolor("lightgreen")
raph.shape("turtle")

#cmd = "FUFDFULFDFUFDLFFFFFF"
cmd = "RRFRFFFLFFLFFFFFF"

for i in cmd:
    ## if the character is 'F', move your turtle forward.
    if i == "F":
        if raph.isdown():
            raph.stamp()
        raph.forward(30)
    ## if the character is 'L', turn your turtle left.
    if i == "L":
        raph.left(90)
    ## if the character is 'R', turn your turtle right.
    if i == "R":
        raph.right(90)
    ## if the character is 'U', lift up the pen.
    if i == "U":
        raph.penup()
    ## if the character is 'D', put the pen down.
    if i == "D":
        raph.pendown()

wn.exitonclick()
