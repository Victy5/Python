from turtle import *
import turtle
import colorsys

turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()

Colors = ["red", "green", "blue", "yellow"]

for i in range(120):
    for c in Colors:
        turtle.color(c)
        turtle.circle(200-i, 100)
        turtle.lt(90)
        turtle.circle(200-i, 100)
        turtle.rt(60)
        turtle.end_fill()

turtle.mainloop()



# speed(0)
# bgcolor("black")
# h = 0.1
# pensize(0)
# def fun():
#     global h
#     for i in range(4):
#         c = colorsys.hsv_to_rgb(h, 2, 2)
#         fillcolor(c)
#         h += 0.004
#         begin_fill()
#         fd(50)
#         rt(20)
#         fd(40)
#         rt(9)
#         end_fill()
# for j in range(100):
#     fun()
#     goto(0, 0)
#     rt(10)
# done()


