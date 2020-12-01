from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILENAME = "data.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def get_high_score(self):
        with open(FILENAME) as data:
            self.high_score = int(data.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open(FILENAME, "w") as data:
            data.write(f"{self.high_score}")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
