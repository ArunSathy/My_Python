# from turtle import *
# import colorsys
# speed(0)
# hideturtle()
# bgcolor('white')
# tracer(5)
# width(2)
# h=0.001
# for i in range(90):
#     color(colorsys.hsv_to_rgb(h,1,1))
#     forward(100)
#     left(60)
#     forward(100)
#     right(120)
#     circle(50)
#     left(240)
#     forward(100)
#     left(60)
#     forward(100)
#     h+=0.02
#     color(colorsys.hsv_to_rgb(h,1,1))
#     forward(100)
#     right(60)
#     forward(100)
#     left(120)
#     circle(-50)
#     right(240)
#     forward(100)
#     right(60)
#     forward(100)
#     left(2)
#     h+=0.02
# done()

#===============================================

import turtle
import colorsys

t=turtle.Turtle()
turtle.Screen().bgcolor('black')
t.pensize(2)
t.speed(9)
n=36
h=0
t.goto(-60,0)
for i in range(20):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.pencolor(c)
    t.circle(105,103)
    t.backward(98)
    t.right(60)
    t.circle(70,68)
    t.left(87)
    t.backward(108)
    t.forward(150)
turtle.done()
