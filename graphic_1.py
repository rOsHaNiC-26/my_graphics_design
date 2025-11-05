from turtle import *
import colorsys

bgcolor("black")
tracer(5) 
hideturtle()
speed(0)


n = 120
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    circle(i * 0.4)
    right(5)
    forward(3)
    h += 1 / n

done()
