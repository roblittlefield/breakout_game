from turtle import Turtle

class Brick(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1.2, stretch_len=4)
        self.penup()
        self.goto(position)

    def brick_break(self):
        self.goto(-500, -500)
