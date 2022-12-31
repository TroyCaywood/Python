import turtle
import pandas

# Setup Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read CSV
states = pandas.read_csv("50_states.csv")
# Create DataFrame
states_df = pandas.DataFrame(states)
# Create score variable
score = 0

answer_state = screen.textinput(title=f"Score: {score}/50", prompt="What's another state's name?")
game_on = True

# Start while loop
while game_on:
    # Loop through states DataFrame rows
    for line in states_df:
        # Check if answer is equal to state series of current row
        if states_df["state"].eq(answer_state).any():
            score += 1
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            # Get current row
            state_name = states_df[states_df.state == answer_state]
            # Get X and Y from current row
            state_x = int(state_name.x)
            state_y = int(state_name.y)
            # Move turtle to current x and y and write state name
            state_turtle.goto(state_x, state_y)
            state_turtle.write(answer_state, font=("Arial", 8, "bold"))

            answer_state = screen.textinput(title=f"Score: {score}/50", prompt="What's another state's name?")
        else:
            answer_state = screen.textinput(title=f"Score: {score}/50", prompt="What's another state's name?")
    print(score)

screen.exitonclick()
