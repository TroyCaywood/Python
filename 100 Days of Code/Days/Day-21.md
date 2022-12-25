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
# Intial random food
food.refresh

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
