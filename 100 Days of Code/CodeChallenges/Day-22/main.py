from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Initial screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")
screen.tracer(0)

scoreboard = Scoreboard()

# Create paddle objects and set initial position. Create ball oblect
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

# Create key listen
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

# While loop for game
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect ball collisions with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        scoreboard.l_increase_score()
        ball.reset_position()

    # Detect if left paddle misses:
    if ball.xcor() < -380:
        scoreboard.r_increase_score()
        ball.reset_position()

screen.exitonclick()
