import turtle
# from turtle import *
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()

turtle.speed(3)
turtle.bgcolor("black")
turtle.pensize(3)
def fun():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('red','pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
fun()
turtle.left(120)
fun()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
