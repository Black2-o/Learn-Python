from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("square")
        self.shapesize(4, 1)
        self.penup()

    def which_go(self, side):
        if side == "left":
            self.goto(350, 0)
        elif side == "right":
            self.goto(-350, 0)

    def move_up(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def move_down(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)
