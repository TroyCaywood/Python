# Day 18 - Turtle & the Graphical User Interface (GUI)

- Just to review, the turtle module is a built in module for drawing graphics on the screen in Python.
- Nobody expects you to memorize all the functions and abilities of a module. That's what the [documentation](https://docs.python.org/3/library/turtle.html) is for.
- In an ideal world, you would read throug the entire documentation before using a module, but that isn't realistic. Sometimes it's easier and faster to search on the internet on sites such as [Stack Overflow](https://stackoverflow.com/) (google search works a little better, just search the term you're looking for followed by site:stackoverflow.com)

- We can also use python to create a Graphical User Interface (GUI) using modules such as [tkinter](https://docs.python.org/3/library/tkinter.html). Turtle actually uses tkinter to create graphics on the screen.

Using the turtle documentation we can create a short program that draws a square on the screen!
```python
from turtle import Turtle, Screen

# Create turtle object
timmie_the_turtle = Turtle()

# Change turtle shape to "turtle" shape
timmie_the_turtle.shape("turtle")

# Change turtle color to plum
timmie_the_turtle.color("plum")

# Move turtle forwards 100 and turn right 4 times
for i in range(4):
    timmie_the_turtle.forward(100)
    timmie_the_turtle.right(90)

# Create screen object
screen = Screen()

# Set screen object to display on until clicked
screen.exitonclick()
```
Now we get a nice plum colored square!

![image ](https://user-images.githubusercontent.com/52113778/209012153-c453de29-f8e9-4e56-865b-8cac49d81bfa.png)

## Different ways to import modules
- There are several ways you can import modules
- You can import the entire module, but then when creating objects you have to call the module name and then the name of the class
```python
import turtle

tim = turtle.Turtle()
```

- You can import whatever you are wanting from the module individually. This makes creating obects a lot faster and easier.
```python
#keyword/ module name/ keyword/ thing in module
from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
```

-You can also import everything from the module using * The disadvantage of this is that it can make it hard to tell where modules came from if you're importing multiple different modules. It's rare to see good code written like this. Try to avoid if you can.
```python
from turtle import *
from random import *

# This is valid and from turtle, but is a bit confusing in isolation
forward(100) 

# Also valid and from random, but it's hard to tell which module it's coming from when reading the code since we imported everything.
choice([1, 2, 3])
```

- You can also import a module as an alias that you define. This can save you some time so you don't have to type out the whole module name or use for clarity.
```ptyhon
import turtle as t

tim = t.Turtle()
```

## Installing Modules
- Not all modules can be imported and must be installed first
- So say you wanted to use the [heroes](https://pypi.org/project/heroes/) module. You can't just import it because it is not a module that is packaged with the standard python library.
- In pycharm, you can type import heroes and then hover over the word heroes and tell pycharm to install the module. Then you can import heroes and use it successfully.
