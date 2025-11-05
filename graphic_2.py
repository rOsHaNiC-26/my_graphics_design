import turtle
import colorsys


t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.hideturtle()
turtle.tracer(10) 


h = 0
while True:
    for c in range(360):
       
        color = colorsys.hsv_to_rgb(h, 1, 1)
        t.pencolor(color)

       
        t.width(c / 200 + 1)
        t.forward(c)
        t.left(100)

      
        h += 0.005

    t.clear() 
