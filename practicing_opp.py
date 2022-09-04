"""
practicing
"""

import random
import turtle as t
from turtle import Screen, Turtle

timmy = Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.color("coral")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# ----------------------- Draw a square----------------------
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dashed line
# for _ in range(15):
#     timmy.pd()
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)

# colors = [
#     "pink",
#     "CornflowerBlue",
#     "DarkOrchid",
#     "DeepSkyBlue",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
#     "IndianRed",
#     "yellow",
#     "purple",
# ]

# ---------------- Draw 10 mf-ing shapes--------------
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)


# -------------- Draw a random walk -----------------
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed(10)

# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# -------------------- Draw a circle --------------------------
# timmy.speed(10)


# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)

# draw_spirograph(5)

# ------------------- Painting Project --------------------


my_screen = Screen()
my_screen.exitonclick()
