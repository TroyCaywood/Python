# Day 20 - Build the Snake Game Part 1: Animation and Coordinates

- Today we are going to start creating the classic [snake game](https://www.playsnake.org) in python
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
