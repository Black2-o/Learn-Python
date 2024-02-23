from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-240, 270)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_refresh(self):
        self.score += 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAme OVer.", align=ALIGNMENT, font=FONT)