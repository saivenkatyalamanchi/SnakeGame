from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.updatescoreboard()
        self.hideturtle()

    def updatescoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", font=("Arial", 24, "normal"), align="center")


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.updatescoreboard()

    def increasescore(self):
        self.score += 1
        self.updatescoreboard()
