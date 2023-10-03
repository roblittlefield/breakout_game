from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from brick import Brick
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -360))
ball = Ball()
scoreboard = Scoreboard()

# Make bricks
brick1_locations = [
    (-500, 330),
    (-400, 330),
    (-300, 330),
    (-200, 330),
    (-100, 330),
    (0, 330),
    (100, 330),
    (200, 330),
    (300, 330),
    (400, 330),
    (500, 330),
]

brick2_locations = [(brick_loc[0]+10, brick_loc[1]-50) for brick_loc in brick1_locations]

brick3_locations = [(brick_loc[0]-10, brick_loc[1]-50*2) for brick_loc in brick1_locations]

brick4_locations = [(brick_loc[0]+10, brick_loc[1]-50*3) for brick_loc in brick1_locations]

brick5_locations = [(brick_loc[0]-10, brick_loc[1]-50*4) for brick_loc in brick1_locations]

bricks1 = []
for i in range(0, len(brick1_locations)):
    (x, y) = brick1_locations[i]
    position = (x, y)
    brick = Brick(position, "red")
    bricks1.append(brick)

bricks2 = []
for i in range(0, len(brick2_locations)):
    (x, y) = brick2_locations[i]
    position = (x, y)
    brick = Brick(position, "orange")
    bricks2.append(brick)

bricks3 = []
for i in range(0, len(brick3_locations)):
    (x, y) = brick3_locations[i]
    position = (x, y)
    brick = Brick(position, "yellow")
    bricks3.append(brick)

bricks4 = []
for i in range(0, len(brick4_locations)):
    (x, y) = brick4_locations[i]
    position = (x, y)
    brick = Brick(position, "green")
    bricks3.append(brick)

bricks5 = []
for i in range(0, len(brick5_locations)):
    (x, y) = brick5_locations[i]
    position = (x, y)
    brick = Brick(position, "blue")
    bricks3.append(brick)

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.bounce_x()
    elif ball.ycor() > 380:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.ycor() < -340 and ball.distance(paddle) < 40:
        ball.bounce_y()

    # Detect paddle miss
    if ball.ycor() < -380:
        ball.reset_position()
        scoreboard.live_lost()
        if scoreboard.lives == 0:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write(f"YOU LOSE. Try again next time.", align="center", font=("Courier", 80, "normal"))

    # Detect collision with brick
    brick_index = -1
    for brick in (bricks1+bricks2+bricks3):
        brick_index += 1
        if ball.distance(brick.pos()) < 50:
            ball.bounce_y()
            brick.brick_break()
            if brick_index <= 10:
                scoreboard.point(1)
                ball.move_speed *= 1.4
            elif brick_index <= 21:
                scoreboard.point(1)
                ball.move_speed *= 1.3
            elif brick_index <= 32:
                scoreboard.point(1)
                ball.move_speed *= 1.2
            elif brick_index <= 43:
                scoreboard.point(1)
                ball.move_speed *= 1.1
            else:
                scoreboard.point(1)

            if scoreboard.score >= 55:
                time.sleep(0.3)
                game_is_on = False
                scoreboard.goto(0, 0)
                scoreboard.write(f"YOU WIN!!!", align="center", font=("Courier", 80, "normal"))
            break


screen.exitonclick()
