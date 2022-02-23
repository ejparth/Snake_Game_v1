from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 13, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.message()

    def message(self):
        self.write(f"SCORE = {self.score}", align=ALIGN, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.message()
