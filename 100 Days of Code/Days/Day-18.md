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
