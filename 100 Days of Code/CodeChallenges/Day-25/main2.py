import turtle
import pandas

# Setup Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


score = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        learn_states = []
        for state in all_states:
            if state not in guessed_states:
                learn_states.append(state)
        learn_states_df = pandas.DataFrame(learn_states)
        learn_states_df.to_csv("learn_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# learn_states = []
# for state in all_states:
#     if state not in answer_state:
#         learn_states.append(state)
#
# learn_states_df = pandas.DataFrame(learn_states)
# learn_states_df.to_csv("learn_states.csv")
