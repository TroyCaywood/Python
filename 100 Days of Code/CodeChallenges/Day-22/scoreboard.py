from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        # Set initial scores
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    # Update scoreboard method. Clears screen, moves scores to correct position and write score
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, font=FONT, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(self.right_score, font=FONT, align=ALIGNMENT)

    # Increase left score by one and update scoreboard
    def l_increase_score(self):
        self.left_score += 1
        self.update_scoreboard()

    # Increase right score by one and update scoreboard
    def r_increase_score(self):
        self.right_score += 1
        self.update_scoreboard()
