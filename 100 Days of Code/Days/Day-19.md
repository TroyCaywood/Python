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
- This is an example of a **higher order function** or a function that can work with other functions. The calculator function is the higher order function because it's taking another function as input and then working with it inside the body of the calculator function.
- It's good practice when using methods that you haven't created yourself to use keyword arguments instead of positional arguments to make your code easier to read.
We can easily look at the first arguements and tell that when the space key is pressed it will call the move_forwards function.
```python
# keyword arguments
screen.onkey(key="space", fun=move_forwards)

# positional arguments
screen.onkey("space", move_forwards)
```
- Using event listeners and the screen.onkey higher order function we can build a little etch-a-sketch type game:
```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
```
- Now we can use the keys w, a, s, and d to draw on the screen and press c to clear the screen:

![image](https://user-images.githubusercontent.com/52113778/209177594-91c3a02e-d5f9-4889-abb8-fc9cd0563c03.png)

## Object State and Instances

- In object oriented programming we can have multiples of the same class assigned to different objects, but they all function separately since it's a new instance of that class:
```python
import turtle

tim = Turtle()
tom = Turtle()
joe = Turtle()

tim.color = "green"
tom.color = "blue"
joe.color = "red"
```
- Each turtle object has a different color assigned to the turtle.color attribue. We would call this the **state** of that attribute for that turtle.
- The state of tim's color attribute is "green" the state of tom's color attribute is "blue" the state of joe's color attribute is "red"
- They could also be doing differeng things like one moving and one is not.
- Each new object is called an **instance**

## Day 19 - [Code Challenge](https://github.com/TroyCaywood/Python/blob/main/100%20Days%20of%20Code/CodeChallenges/Day-19/Day_19-TurtleRace.py) - Turtle Race - You pretty much walk through this one in the lesson today. I'd suggest finishing the lesson before you click.
