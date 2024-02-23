from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)
snake = Snake()
boarder = Border()
food = Food()
my_score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Snake with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        my_score.score_refresh()

        snake.snake_extend()
        screen.tracer(0)

    # Detect Snake with Wall
    if snake.head.xcor() > 275 or snake.head.xcor() < -275 or snake.head.ycor() > 245 or snake.head.ycor() < -270:
        my_score.reset()
        snake.reset()

    # Detect Snake with his own tail.
    for snake_body in snake.snake_list[1:]:
        # if snake_body == snake.head:
        #     pass
        if snake.head.distance(snake_body) < 10:
            my_score.reset()
            snake.reset()

screen.exitonclick()
