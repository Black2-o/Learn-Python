from turtle import Turtle, Screen


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(10)
        self.penup()
        self.goto(275, 0)
        self.pendown()
        self.goto(275, 245)
        self.goto(-275, 245)
        self.goto(-275, -275)
        self.goto(275, -275)
        self.goto(275, 0)
        self.hideturtle()
