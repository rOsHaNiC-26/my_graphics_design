import turtle as tur
import colorsys
import time
import math

# --- Setup ---
tur.bgcolor("black")
tur.speed(0)
tur.tracer(0)
tur.hideturtle()
tur.width(2)
tur.setup(700, 700)

# --- Function to draw glowing triangle pattern ---
def draw_triangle_spiral(rot, scale, hue_shift):
    tur.clear()
    n = 150  # number of triangles
    for i in range(n):
        hue = (i / n + hue_shift) % 1.0
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        tur.pencolor(color)
        for j in range(3):
            tur.forward(100 * scale)
            tur.right(70)
        tur.right(3 + rot)
    tur.update()

# --- Animation Loop ---
frame = 0
angle = 0
while True:
    # Smooth breathing / zoom effect
    scale = 1 + 0.2 * math.sin(frame / 20)
    hue_shift = (frame % 360) / 360  # slowly shifts colors
    draw_triangle_spiral(angle, scale, hue_shift)

    angle += 0.5   # rotation speed
    frame += 1
    time.sleep(0.03)
