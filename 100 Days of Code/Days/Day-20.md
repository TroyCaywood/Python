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
