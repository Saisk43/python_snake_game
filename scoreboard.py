from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../OneDrive/Desktop/data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.board()

    def board(self):
        self.clear()
        self.write(arg=f"score: {self.score} High score: {self.high_score}", align="center", font=("courier", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../OneDrive/Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.board()

    def increase_score(self):
        self.score += 1
        self.board()
