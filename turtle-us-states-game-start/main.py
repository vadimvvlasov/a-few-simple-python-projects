import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data['state'].to_list()
print(all_states)
correct_guesses = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)} / {len(all_states)} States Correct",
                                    prompt="what's another state's name? ").title()
    if answer_state == "Exit":
        states_to_learn = set(all_states) - set(guessed_states)
        pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

