# Day 19 - Instances, State and Higher Order Functions



## Event Listeners

- The turtle function has a listen method that accepts keyboard inputs. It "listens" for the user to press a key and then executes a function.

This code will move the turtle forward 10 paces when spacebar is pressed
```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
```


## Functions as Inputs
- When using a function as an argument in another function you do not add the parenthesis to the function that is the argument
```python
def function_a(something):
  # Do this with something
  # Then do this
  # Finally do this

def function_b():
  # Do this

function_a(function_b)
```
- We could use this for something like a calculator function where all we have to do is swap out the numbers and the function name:
```python
def add(n1, n2):
  return n1 + n2
  
def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1/n2
 
def calculator(n1, n2, func):
  return func(n1, n2)
  
result = calculator(2, 3, add)
# This would print 5 since 2 + 3 = 5
print(result)
```
