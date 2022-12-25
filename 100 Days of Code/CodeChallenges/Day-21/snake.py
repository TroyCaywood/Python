from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in POSITIONS:
      self.add_segment(position)

  def add_segment(self, position):
    self.new_snake = Turtle("square")
    self.new_snake.penup()
    self.new_snake.color("white")
    self.new_snake.goto(position)
    self.segments.append(self.new_snake)

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def move(self):
    # Move each segment to the position of the segment before it and then move the first segment forwards outside of for loop to get the segments sto follow each other
    for seg_num in range (len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
