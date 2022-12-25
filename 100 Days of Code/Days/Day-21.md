# Day 21 - Build the Snake Game Part 2: Inheritance and List Slicing

- Today we are going to finish creating the classic [snake game](https://www.playsnake.org) in python
- Yesterday we completed the first 3 steps and will work on the remaining steps today:
   + ~~Create the snake body out of 3 squares on the screen lined up next to each other~~
   + ~~Tell the snake to move forwards constantly~~
   + ~~Create controls to move the snake~~
   + Put food on the screen and detect collision between the snake and food and then get rid of that piece of food and create it again in a new random location
   + Create a scoreboard to keep score
   + Create a game over situation when the snake hits the wall
   + Game over when the snake hits itself

- To do so we will need to learn a couple of new concepts first.

## Class Inheritance

- Classes can inherit behavior and appearance from other classes
- For example, the Fish class is inheriting everything from the Animal class. To do so we call the Animal class when defining the Fish class in the parenthesis and then in the initialization for the Fish class we call `super().__init__()` the super refers to the super class which is Animal in this case and causes the Fish class to inherit all of the methods and attributes from Animal.
```python
class Animal(self):
   def __init__(self):
      self.num_eyes = 2
      
   def breathe(self):
      print("Inhale, exhale.")
     
class Fish(Anmial):
   def __init__(self):
      super().__init__()
      
   def breathe(self):
      super().__init__()
      print("Doing this underwater.")
      
   def swim(self):
      print("Moving in water.")
      
nemo = Fish()
# From Fish class prints 'Moving in water.'
nemo.swim
# From Animal superclass prints 'Inhale, exhale.' and 'Doing this underwater.' since we modified it.
nemo.breathe
# From animal superclass prints '2'
print(nemo.num_eyes)
```
- Now we can call all the methods and attributes from Animal on a Fish object since we told fish to initialize everything from Animal.

## Detect Collisions with Food
- Now we can get back to our snake game and work on setting up the food portion of the game.
- First we are going to create a new food.py file and create the Food class and have it inherit everyting from the Turtle class. That way we can do things like `self.shape("circle")`
```python
from turtle import Turtle

class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
```
Now we can add the rest of the attributes and tell the food to go to a random spot on the screen
```python
from turtle import Turtle
import random

class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    # Change size to 10x10 instead of 20x20
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    # Create random ints for x and y positions
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    # Tell dot to go to random x and y position
    self.goto(random_x, random_y)
  ```
  Then we can import Food into our main.py and we don't need Turtle in main.py anymore so we can stop importing it and create a Food variable
  ```python
  from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)

snake = Snake()
food = Food()

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
- Now we need to tell the food to move every time the snake touches it. We do this using the `snake.head.distance(food)' this measures the distance from the head of our snake to the food. We'll say if the head is less than 15 pixels away then we'll move the food. First we need to create a method in our Fish class to do that. We'll just move the random x and y and goto into that method.

```python
from turtle import Turtle
import random

class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    # Change size to 10x10 instead of 20x20
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    food.refresh()

  def refresh(self):
    # Create random ints for x and y positions
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    # Tell dot to go to random x and y position
    self.goto(random_x, random_y)
```
and our main.py now looks like this
```python
from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)

snake = Snake()
food = Food()

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

  # Detect collisions with food by measuring distance from head to food
  if snake.head.distance(food) < 15:
    # Move food to a new location
    food.refresh()


screen.exitonclick()
```

## Create Scoreboard and Keep Score
- Now we can create a scoreboard.py file and create the Scoreboard class utilizing the Turtle.write() method
```python
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    # Set penup so we don't see the line when we move the turtle
    self.penup()
    # Move turtle to the top of the screen
    self.goto(0, 270)
    # Set color to white so we can see the text
    self.color("white")
    # Hide the turtle graphic
    self.hideturtle()
    # Set initial score to 0
    self.score = 0
    # Call update_scoreboard method
    self.update_scoreboard()

   # Create update_scoreboard method that writes Score: and then the current score at the top of the screen
  def update_scoreboard(self):
    self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
  
  # Create method to increase score by adding 1 to the score attribute and then clear the screen and write the new score
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()
```
- Now all we have to do is import our new Scoreboard class and call the increase_score method when the snake hits the food
```python
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard= Scoreboard()
# Intial random food
food.refresh
scoreboard

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

  # Detect collisions with food by measuring distance from head to food
  if snake.head.distance(food) < 15:
    # Move food to a new location
    food.refresh()
    # Increase score when snake touches food
    scoreboard.increase_score()

screen.exitonclick()
```

## Detect Collisions with the Wall
- Now we need to make the game end when the snake hits the wall. We'll do this by detecting when the snake head is at over 280 x or y coordinate and under -280 x or y coordinate and then we'll call a game_over method that we define in our scoreboard class.
```python
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.goto(0, 270)
    self.color("white")
    self.hideturtle()
    self.score = 0
    self.update_scoreboard()

  def update_scoreboard(self):
    self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
  
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()

  def game_over(self):
    self.goto(0, 0)
    self.write("Game OVER!", font=FONT, align=ALIGNMENT)
```
In our main.py
```python
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard= Scoreboard()
# Intial random food
food.refresh
scoreboard

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

  # Detect collisions with food by measuring distance from head to food
  if snake.head.distance(food) < 15:
    # Move food to a new location
    food.refresh()
    scoreboard.increase_score()

  # Detect collisions with the wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    # Stop the game
    game_is_on = False
    # Print game over
    scoreboard.game_over()

  
screen.exitonclick()
```
## Detect Collisions with Self
- Now we need to make a way for the game to detect when the snake hits itself when it gets too long and also create a way for the snake to grow.
- First lets create a way to make our snake grow one segment by editing our snake.py file and creating a add_segment method and extend method
```python
from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
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
      self.add_segment(position)

  # Create add_segment method
  def add_segment(self, position):
    self.new_snake = Turtle("square")
    self.new_snake.penup()
    self.new_snake.color("white")
    self.new_snake.goto(position)
    self.segments.append(self.new_snake)
   
   # Add one segment behind the last segment
  def extend(self):
    self.add_segment(self.segments[-1].position())

  def move(self):
    # Move each segment to the position of the segment before it and then move the first segment forwards outside of for loop to get the segments sto follow each other
    for seg_num in range (len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

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
- Now all we have to do is add our extend method to main.py when the snake touches food
```python
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard= Scoreboard()
# Intial random food
food.refresh
scoreboard

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

  # Detect collisions with food by measuring distance from head to food
  if snake.head.distance(food) < 15:
    # Move food to a new location
    food.refresh()
    # Extend snake when it touches food
    snake.extend()
    scoreboard.increase_score()

  # Detect collisions with the wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()

  
screen.exitonclick()
```

## Detect Collisions with self
- Now we need to create a way for the snake to detect collisions with itself and end the game. We'll do that by adding this to our main.py
```python
# Detect collisions with tail
   # Loop through segments in snake.segments list
  for segment in snake.segments:
    # Skip the head segment
    if segment == snake.head:
      pass
     # If the distance from the head to any segment is less than 10 pixels end the game
    elif snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()
```
