from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 14, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Your score is {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"   GAME OVER\n\n\nYour score was {self.score}", align=ALIGNMENT, font=FONT)

    def clear_score(self):
        self.score += 1
        self.clear()
        self.update_score()
