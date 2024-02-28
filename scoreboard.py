from turtle import Turtle

FONT = ('Arial', 16, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.increase_score()

    def increase_score(self):
        self.goto(0, 270)
        self.write(arg=f"Score: {self.points}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def score(self):
        self.points += 1
        self.clear()
