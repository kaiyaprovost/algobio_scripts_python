import math

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

raph=turtle.Turtle()
raph.color("red")
raph.shape("turtle")

mikey=turtle.Turtle()
mikey.color("orange")
mikey.shape("turtle")
mikey.left(90)

leo=turtle.Turtle()
leo.color("blue")
leo.shape("turtle")
leo.left(180)

don=turtle.Turtle()
don.color("purple")
don.shape("turtle")
don.left(270)


for i in range(50,131,10):
    raph.forward(i)
    mikey.forward(i)
    leo.forward(i)
    don.forward(i)
 
    raph.left(95)
    mikey.left(95)
    leo.left(95)
    don.left(95)
 
    raph.forward((i/5.71428))
    mikey.forward((i/5.71428))
    leo.forward((i/5.71428))
    don.forward((i/5.71428))
 
    raph.left(95)
    mikey.left(95)
    leo.left(95)
    don.left(95)
 
    raph.forward(i)
    mikey.forward(i)
    leo.forward(i)
    don.forward(i)
 
    raph.left(10)
    mikey.left(10)
    leo.left(10)
    don.left(10)
