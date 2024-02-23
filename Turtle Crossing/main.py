import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Screen 
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)


#Player
player = Player()
player.startFrom()
screen.onkey(player.move, "Up")

# Others 
car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car_maker()
    car.move()
    for carX in car.all_car:
        if player.distance(carX) < 20:
            print("Detect")
            game_is_on = False
            score.game_over()

    if player.ycor() >= 280:
        player.reset_game()
        car.moveN()
        score.score_refresh()

screen.exitonclick()