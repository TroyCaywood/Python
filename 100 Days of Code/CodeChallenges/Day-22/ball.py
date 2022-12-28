from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    # Define ball movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Reverse y movement and decrease move speed
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    
    # Reverse x movement and increase move speed
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Reset ball position to center and reset move speed and bounce in opposite direction
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
