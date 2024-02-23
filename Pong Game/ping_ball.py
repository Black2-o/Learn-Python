from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        newX = self.xcor() + self.x_move
        newY = self.ycor() + self.y_move
        self.goto(newX, newY)

    def bounceY(self):
        self.y_move *= -1

    def bounceX(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(00.00, 00.00)
        self.bounceX()
        self.move_speed = 0.1
