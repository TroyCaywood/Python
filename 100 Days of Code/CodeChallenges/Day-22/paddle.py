from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=None)
        self.penup()
        self.goto(position)
    
    # Define up movement method
    def up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)
    
    # Define down movement method
    def down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
