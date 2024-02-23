from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("database.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_refresh(self):
        self.score += 1
        self.score_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("database.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAme OVer.", align=ALIGNMENT, font=FONT)
