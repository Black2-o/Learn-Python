import turtle
from turtle import Turtle, Screen
import random

import turtle as t

turtle = Turtle()

# turtle.shape("classic")
# for _ in range(0, 20):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# num_sides = 5
#
#
# def draw_shapes(num_sides):
#     angel = 360 / num_sides
#     for _ in range(num_sides):
#         turtle.forward(100)
#         turtle.right(angel)
#
#
# turtle_color = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue", "LimeGreen", "wheat", "SlateGray", "SeaGreen",
#                 "IndianRed"]
# for shape_side in range(3, 11):
#     turtle.color(random.choice(turtle_color))
#     draw_shapes(shape_side)


## Random Make

# turtle.width(10)
# turtle_color = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue", "LimeGreen", "wheat", "SlateGray", "SeaGreen", ]
# turtle.speed("fastest")
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     turtle_color = (r, g, b)
#     return turtle_color
#
#
# def which_side_go():
#     side = ["left", "right", "up", "down"]
#     side_go = random.choice(side)
#     if side_go == "left":
#         return 360
#     elif side_go == "right":
#         return 180
#     elif side_go == "up":
#         return 90
#     elif side_go == "down":
#         return 270
#
#
# for _ in range(100):
#     x = which_side_go()
#     turtle.color(random_color())
#     turtle.forward(25)
#     turtle.left(x)
#

# Circle Maker
t.colormode(255)
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r, g, b)
    return turtle_color


def draw(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw(5)

screen = Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())
