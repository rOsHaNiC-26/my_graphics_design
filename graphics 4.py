import turtle
color=["red","purple",
       "blue","green",
       "orange","yellow"]
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("maroon")
for c in range(300):
    t.pencolor(color[c%6])
    t.width(c/200+1)
    t.forward(c)
    t.left(100)
