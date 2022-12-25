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
