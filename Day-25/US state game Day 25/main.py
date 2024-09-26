import turtle
from importlib.machinery import all_suffixes

import pandas


screen = turtle.Screen()
my_turtle = turtle.Turtle()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image) # used to add the image as the background of the turtle screen..
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50", prompt= "What's another state's name?").title()
    # print(answer_state)
    if answer_state == "Exit":
        # Generating the CSV file for the missed states
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        """USING THE LIST COMPREHENSION"""
        missing_states = [states for states in all_states if states not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # print(state_name)
        # cor_x = (state_name["x"].item()) # when only state_name["x"] is written then it give both index
        # # and the co-ordinate which is not suitable for goto method so we need item()
        # cor_y = (state_name["y"].item())
        # print(f"{cor_x}, {cor_y}")
        # title_answer = answer_state.title()
        # print(type(cor_x))
        state_data = data[data.state == answer_state]

        my_turtle.penup()
        my_turtle.hideturtle()
        my_turtle.goto(state_data.x.item(), state_data.y.item())
        my_turtle.write(f"{answer_state}", font=("Arial", 8, "normal"))


