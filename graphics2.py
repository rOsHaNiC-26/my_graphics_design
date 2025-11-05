import turtle
t=turtle.Turtle()

def triangle(l,a):
    for i in range(3):
        t.forward(l)
        t.right(a)
        
for i in range(150):
    triangle(100,70)
    t.right(3)
t.done()
