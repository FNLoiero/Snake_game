from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 14, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.file_score = open("high_score.txt", mode = "r")
        self.highscore = int(self.file_score.read())
        self.file_score.close()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Your score is {self.score} High score {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

    def update_file_score(self):
        file_score = open("high_score.txt", mode = "w")
        file_score.write(f"{self.highscore}")
        file_score.close()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"   GAME OVER\n\n\nYour score was {self.score}", align=ALIGNMENT, font=FONT)

    def clear_score(self):
        self.score += 1
        self.clear()
        self.update_score()
