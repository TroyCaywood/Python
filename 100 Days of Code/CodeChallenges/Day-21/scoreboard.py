from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.goto(0, 270)
    self.color("white")
    self.hideturtle()
    self.score = 0
    self.update_scoreboard()

  def update_scoreboard(self):
    self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
  
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()

  def game_over(self):
    self.goto(0, 0)
    self.write("Game OVER!", font=FONT, align=ALIGNMENT)
