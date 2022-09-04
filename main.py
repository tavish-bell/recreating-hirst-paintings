# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import random
import turtle as t
from turtle import Screen, Turtle, pen

bert = Turtle()
t.colormode(255)
bert.shape("turtle")
bert.color("coral")


color_list = [
    (191, 164, 139),
    (208, 195, 183),
    (143, 90, 67),
    (72, 108, 128),
    (203, 192, 177),
    (150, 68, 80),
    (137, 166, 153),
    (69, 111, 89),
    (184, 90, 100),
    (128, 157, 165),
    (188, 99, 88),
    (179, 138, 146),
    (153, 142, 70),
    (77, 152, 119),
    (110, 45, 51),
    (63, 50, 57),
    (58, 55, 49),
    (209, 185, 177),
    (54, 54, 61),
    (92, 142, 155),
    (35, 69, 41),
    (120, 120, 144),
    (113, 46, 43),
    (45, 76, 51),
    (71, 64, 53),
    (57, 59, 77),
    (209, 193, 196),
    (207, 181, 184),
    (192, 199, 193),
    (185, 196, 186),
]

bert.setheading(0)
bert.speed(10)
bert.penup()
bert.setheading(225)
bert.forward(300)
bert.setheading(0)


def painting(space, x, y):
    for _ in range(x):
        for _ in range(y):
            bert.dot(20, random.choice(color_list))
            bert.forward(space)
        bert.backward(50 * 10)
        bert.left(90)
        bert.forward(space)
        bert.right(90)
        bert.resizemode("user")


painting(50, 10, 10)


my_screen = Screen()
my_screen.exitonclick()
