from turtle import Screen, Turtle
from paddle import Paddle
from ping_ball import Ball
from scoreboard import Scoreboard
import time

# Screen work
screen = Screen()
screen.listen()
screen.tracer(0)
screen.title("Pong Game.")
screen.bgcolor("black")
screen.setup(width=800, height=600)


# Left Paddle Make & Make It's Behabiour
r_paddle = Paddle()
r_paddle.which_go("left")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# Right nd Paddle Make & Make It's Behabiour
l_paddle = Paddle()
l_paddle.which_go("right")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


# Ping Ball
ball = Ball()
# ScoreBoard
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detexting The Wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        # Needs to Bounce
        ball.bounceY()

    # Deceting with the Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 30 and ball.xcor() > -380:
        print("Made Contact")
        ball.bounceX()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
