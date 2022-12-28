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
- Now lets create a ball class and have it move to the top right corner of the screen
```python
# Ball Class
from turtle import Turtle
import time

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("circle")
    self.color("white")
    
  # Move to top right corner
  def move(self):
    new_x = self.xcor() + 10
    new_y = self.ycor() +10
    self.goto(new_x, new_y)
```
This is what main.py looks like now
```python
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")
# Turn off screen update to hide paddles moving into position
screen.tracer(0)

# Create Paddle objects and pass position arguments and create ball object
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()




# Create paddle movement keys
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

# Turn on screen update so we can see everything on the screen slow down time a little and move ball
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
```
## Detect Collisions with Wall and Bounce
- Now we need to add the ability for the ball to detect collisions with the wall and bounce
- First we'll add an if statement to the main.py in the `while game_is_on:` loop
```python
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
  # Detect ball collisions with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce()
```
and here is what we did in our ball class to make the y-coordinates reverse. We just multiply them by -1
```python
from turtle import Turtle

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("circle")
    self.color("white")
    self.x_move = 10
    self.y_move = 10
    

  def move(self):
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(new_x, new_y)

  # Multiply y_move by -1 to reverse the number
  def bounce(self):
    self.y_move *= -1
```
## Detect Collisions with Paddles

- Now we need a way to detect collisions with the paddles and make the ball bounce off of them. 
- First we'll change our bounce method in the ball class to have a bounce_x and bounce_y method:
```python
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
```
- Now we'll add an if statement to our while loop that checks the distance of the ball from the paddle and then calls the bounce_x method
```python
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
```

- Now the ball bounces off the walls and the paddles as we expect it to

# Detect When Paddles Miss
- Now we need to detect when a paddle misses the ball, reset the ball to the center, and reverse the direction
- First we'll define a reset_position method in the ball class
```python
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
```
- Then we'll setup an if condition for the left and right paddles in our while loop:
```python
    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect if left paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
```

## Scoreboard

- Now lets setup a scoreboard class

```python
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        # Set initial scores
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    # Update scoareboard method. Clears screen, moves scores to correct position and write score
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, font=FONT, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(self.right_score, font=FONT, align=ALIGNMENT)
    
    # Increase left score by one and update scoreboard
    def l_increase_score(self):
        self.left_score += 1
        self.update_scoreboard()
    
    # Increase right score by one and update scoreboard
    def r_increase_score(self):
        self.right_score += 1
        self.update_scoreboard()
```
- Now in our main.py lets add the increase score methods when each paddle misses
```python
    # Detect if right paddle misses
    if ball.xcor() > 380:
        scoreboard.l_increase_score()
        ball.reset_position()

    # Detect if left paddle misses:
    if ball.xcor() < -380:
        scoreboard.r_increase_score()
        ball.reset_position()
```
- To make the game more challenging we'll increase the speed of the ball a little bit every time a paddle hits the ball we'll do this by adding a `self.move_speed = 0.1` to our ball class and then multiply the move speed by 0.9 every time it bounces. Then on `reset_position` we'll change it back to 0.1

## See the completed code [here](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day-22)

