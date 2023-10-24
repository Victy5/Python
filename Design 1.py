from turtle import *
import colorsys
import math
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3*k)-\
            math.cos(4*k)
speed(1000)
bgcolor("black")
h = 0
for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)
    for j in range(5):
        h+= 0.002
        color(colorsys.hsv_to_rgb(h, 1, 1))
    goto(0,0)
done()