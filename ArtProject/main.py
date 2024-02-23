import turtle
from turtle import Turtle, Screen
import random
color_listX = [(209, 165, 125), (249, 234, 237), (140, 48, 106), (164, 169, 38),
               (244, 80, 56), (3, 143, 55), (233, 109, 162), (215, 234, 232),
               (241, 65, 140), (1, 143, 184), (162, 55, 52), (57, 202, 224),
               (254, 230, 0), (20, 166, 126), (211, 232, 236), (244, 223, 50),
               (27, 197, 219), (162, 184, 171), (233, 165, 191)]


turtleX = Turtle()
turtle.colormode(255)
turtleX.penup()
turtleX.setposition(-300.00, -200.00)
turtleX.hideturtle()


def go_horizontal():
    for _ in range(10):
        turtleX.fd(50);
        turtleX.dot(25, random.choice(color_listX))


def go():
    go_vertical = -150.00
    for _ in range(10):
        go_horizontal()
        turtleX.setposition(-300.00, go_vertical)
        go_vertical += 50.00


go()

screen = Screen()
screen.exitonclick()
