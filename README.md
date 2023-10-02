# Breakout Game
## by Rob Littlefield

### Creating the board
The board is created using Turtle graphics geometric drawing tool.
```python
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=1000)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -260))
ball = Ball()
scoreboard = Scoreboard()

# Make bricks
brick1_locations = [
    (-300, 230),
    (-200, 230),
    (-100, 230),
    (0, 230),
    (100, 230),
    (200, 230),
    (300, 230),
]

brick2_locations = [(brick_loc[0]+5, brick_loc[1]-50) for brick_loc in brick1_locations]

brick3_locations = [(brick_loc[0]-5, brick_loc[1]-50*2) for brick_loc in brick1_locations]

bricks1 = []
for i in range(0, len(brick1_locations)):
    (x, y) = brick1_locations[i]
    position = (x, y)
    brick = Brick(position, "red")
    bricks1.append(brick)

bricks2 = []
for i in range(0 , len(brick2_locations)):
    (x, y) = brick2_locations[i]
    position = (x, y)
    brick = Brick(position, "orange")
    bricks2.append(brick)

bricks3 = []
for i in range(0 , len(brick3_locations)):
    (x, y) = brick3_locations[i]
    position = (x, y)
    brick = Brick(position, "green")
    bricks3.append(brick)

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
```

### Creating the Paddle
The paddle can move left and right when the keyboard left and right arrows are pressed. The paddle bounces the ball back up in a positive direction on the Y-axis.
```python
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 50
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 50
        self.goto(new_x, self.ycor())
```

### Creating the Bricks
The bricks are creating using a position array that then loops through a Brick class to create the brick layers. The bricks further up speed up the ball when they are destroyed. The bricks are colored differently based on their location and whether they speed up the ball when destroyed.
```python
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
```

### Creating the Ball
The ball is contained within the game walls and will bounce off the top, left and right sides. It's speed is dependent on how many of the orange and red bricks have been destroying, increaseing in speed as the game goes on.
```python
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_y()
```

### Creating the Scoareboard
The Scoreboard class keeps a count of the number of player lives left and the player score, which increases as more bricks are destroyed. 
```python
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 5
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-252, 268)
        self.write(f"Lives: {self.lives}, Score: {self.score}", align="center", font=("Courier", 25, "normal"))

    def point(self, amount):
        self.score += 1 * amount
        self.update_scoreboard()

    def live_lost(self):
        self.lives -= 1
        self.update_scoreboard()
```

### Gameplay and Scoring
If the ball misses the ball and falls to the bottom side, the player loses a life. Destroying bricks adds points to the player score. 
```python
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    elif ball.ycor() > 280:
        ball.bounce_y()

    # Detect collion with paddle
    if ball.ycor() < -240 and ball.distance(paddle) < 40:
        ball.bounce_y()

    # Detect paddle miss
    if ball.ycor() < -280:
        ball.reset_position()
        scoreboard.live_lost()

    # Detect collision with brick
    brick_index = -1
    for brick in (bricks1+bricks2+bricks3):
        brick_index += 1
        if ball.distance(brick.pos()) < 50:
            ball.bounce_y()
            brick.brick_break()
            if brick_index <= 6:
                scoreboard.point(3)
                ball.move_speed *= 1.4
            elif brick_index <= 13:
                scoreboard.point(2)
                ball.move_speed *= 1.2
            else:
                scoreboard.point(1)

            if scoreboard.score >= 42:
                time.sleep(0.3)
                game_is_on = False
                scoreboard.goto(0, 0)
                scoreboard.write(f"YOU WIN!!!", align="center", font=("Courier", 80, "normal"))
            break

screen.exitonclick()
```
