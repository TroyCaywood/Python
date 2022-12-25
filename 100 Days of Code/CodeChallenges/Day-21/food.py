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
    self.refresh()

  def refresh(self):
    # Create random ints for x and y positions
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    # Tell dot to go to random x and y position
    self.goto(random_x, random_y)
