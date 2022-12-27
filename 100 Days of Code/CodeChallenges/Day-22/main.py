from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")
screen.tracer(0)

right_paddle = Paddle()
right_paddle.new_paddle.setposition(350, 0)

left_paddle = Paddle()
left_paddle.new_paddle.setposition(-350, 0)

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
