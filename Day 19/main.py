import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
user_guess = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "IndianRed"]
all_turtle = []
screen.setup(width=500, height=400)
x = -225
y = 150
color = 0
for turtle_name in colors:
    turtle_name = Turtle(shape="turtle")
    turtle_name.penup()
    turtle_name.color(colors[color])
    turtle_name.goto(x, y)
    y -= 50
    color += 1
    all_turtle.append(turtle_name)

if user_guess:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is won the race!")
            else:
                print(f"You've lost! The {winning_color} turtle is won the race!")
        turtle.forward(random.randint(0,10))




# turtleX.speed("fastest")

#
# def move_forwards():
#     turtleX.forward(10)
#
#
# def move_backward():
#     turtleX.backward(10)
#
#
# def move_left():
#     turtleX.left(20)
#
#
# def move_right():
#     turtleX.right(20)
#
#
# def clear():
#     turtleX.clear()
#     turtleX.penup()
#     turtleX.home()
#     turtleX.pendown()
#
#
# screen.listen()
#
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(clear, "c")


screen.exitonclick()
