from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-450, 368)
        self.write(f"Lives: {self.lives}, Score: {self.score}", align="center", font=("Courier", 25, "normal"))

    def point(self, amount):
        self.score += 1 * amount
        self.update_scoreboard()

    def live_lost(self):
        self.lives -= 1
        self.update_scoreboard()
