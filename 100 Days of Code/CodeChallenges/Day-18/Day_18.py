from turtle import Turtle, Screen
import random

# Create turtle object
tim = Turtle()

# Change turtle shape to "turtle" shape
tim.shape("turtle")

# Change turtle color to plum

tim.pencolor(
        float(random.randint(1, 255)),
        float(random.randint(1, 255)),
        float(random.randint(1, 255))
        )
print(type(timmy))

# Move turtle forwards 100 and turn right 4 times
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# Create screen object
screen = Screen()

# Set screen object to display on until clicked
screen.colormode(255)
screen.exitonclick()
