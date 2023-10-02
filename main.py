from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from brick import Brick
import time

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
