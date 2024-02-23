from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_car = []

        

    def car_maker(self):
        random_choice = random.randint(0, 6)
        if random_choice == 1 or random_choice == 3:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(320, random.randint(-250, 250))
            car.left(180)
            self.all_car.append(car)

    def move(self):
        for x in self.all_car:
            x.forward(STARTING_MOVE_DISTANCE)

    def moveN(self):
        now_move = 5
        for x in self.all_car:
            now_move += MOVE_INCREMENT
            x.forward(STARTING_MOVE_DISTANCE)
