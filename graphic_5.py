import turtle
import colorsys

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)

h = 0
for i in range(400):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    t.forward(i)
    t.left(91)
    h += 0.005  # gradual color shift

turtle.done()
