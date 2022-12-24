# Day 20 - Build the Snake Game Part 1: Animation and Coordinates

- Today we are going to start creating the classic [snake game](https://www.playsnake.org) in python
- This day includes a lot of challenges so I suggest going through the video before reading this section.
- To do so we will break it down into steps:
   + Create the snake body out of 3 squares on the screen lined up next to each other
   + Tell the snake to move forwards constantly
   + Create controls to move the snake
   + Put food on the screen and detect collision between the snake and food and then get rid of that piece of food and create it again in a new random location
   + Create a scoreboard to keep score
   + Create a game over situation when the snake hits the wall
   + Game over when the snake hits itself
  
## Creating the initial snake
- First we need to create our starting snake body:
```python
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")

# List of position tuples for snake segments
positions = [(0, 0), (-20, 0), (-40, 0)]

# Create 3 new snake objects and move them to the correct locations
for snake in range(3):
  new_snake = Turtle("square")
  new_snake.penup()
  new_snake.color("white")
  new_snake.goto(positions[turtle])



screen.exitonclick()
```
- Now we need to get the snake segments to follow each other:
```python
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in positions:
  new_snake = Turtle("square")
  new_snake.penup()
  new_snake.color("white")
  new_snake.goto(position)
  segments.append(new_snake)

# update screen
screen.update()

game_is_on = True
while game_is_on:
  # Update screen outside of for loop
  screen.update()
  # Slow down speed
  time.sleep(0.1)
  # Move each segment to the position of the segment before it and then move the first segment forwards outside of for loop to get the segments sto follow each other
  for seg_num in range (len(segments) - 1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(new_x, new_y)
  segments[0].forward(20)




screen.exitonclick()
```
- Now we can clean up our code by creating a snake class in snake.py
```py
from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()

  def create_snake(self):
    for position in POSITIONS:
      self.new_snake = Turtle("square")
      self.new_snake.penup()
      self.new_snake.color("white")
      self.new_snake.goto(position)
      self.segments.append(self.new_snake)

  def move(self):
    for seg_num in range (len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.segments[0].forward(MOVE_DISTANCE)
```
- This makes our main.py a lot shorter and easier to read
```python
from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
  # Update screen outside of for loop
  screen.update()
  # Slow down speed
  time.sleep(0.1)
  
  snake.move()


screen.exitonclick()
```
- Now we can create a way to move the snake around the screen:
```python
from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Set heading directions constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in POSITIONS:
      self.new_snake = Turtle("square")
      self.new_snake.penup()
      self.new_snake.color("white")
      self.new_snake.goto(position)
      self.segments.append(self.new_snake)

  def move(self):

      # Move each segment to the position of the segment before it and then move the first segment forwards outside of for loop to get the segments sto follow each other
    for seg_num in range (len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)
   
   # Since we really only care about where the head is pointing since all the other segments follow it, we can change the heading of the head to the different direction headings 
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
```
- Then add the new methods to our main.py

```python
from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)

snake = Snake()

# Start listening for up down left and right key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  # Update screen outside of for loop
  screen.update()
  # Slow down speed
  time.sleep(0.1)
  
  snake.move()


screen.exitonclick()
```
- Look at that! We can move our snake around now! Neato.

## No code challenge today since we walk through this code together.
