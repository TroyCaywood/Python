from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):

        super().__init__()
        self.create_paddle()


    def create_paddle(self):
        self.new_paddle = Turtle("square")
        self.new_paddle.color("white")
        self.new_paddle.turtlesize(stretch_wid=5, stretch_len=1, outline=None)
        self.new_paddle.penup()

    def up(self):
        self.new_paddle.new_y = self.new_paddle.ycor() + 20
        self.new_paddle.goto(self.new_paddle.xcor(), self.new_paddle.new_y)

    def down(self):
        self.new_paddle.new_y = self.new_paddle.ycor() - 20
        self.new_paddle.goto(self.new_paddle.xcor(), self.new_paddle.new_y)
