# Day 22 - Build Pong: The Famous Arcade Game

- Today we will be building a clone of the classic [pong](https://en.wikipedia.org/wiki/Pong) arcade game.
- The steps to do this will be
  + Create the screen
  + Create and move a paddle
  + Create another paddle
  + Create the ball and make it move
  + Detect collision with wall and bounce
  + Detect collision with paddle
  + Detect when paddle misses
  + Keep score  

## Create the screen and paddles

- First lets take care of creating our play screen and the two paddles and how to control them:
```python
# Main.py
from screen import Screen
from paddle import Paddle

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")
# Turn off screen update to hide paddles moving into position
screen.tracer(0)

# Create Paddle objects and pass position arguments
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Create paddle movement keys
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

# Turn on screen update so we can see everything on the screen
while game_is_on:
    screen.update()

screen.exitonclick()
````
And our paddle class
```python
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=None)
        self.penup()
        self.goto(position)

    def up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
```

# Create Ball Class and Movement
