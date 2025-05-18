import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
turtle.penup()

data = pandas.read_csv('50_states.csv')
all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ {len(all_states)} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        tim = Turtle()
        tim.hideturtle()
        tim.penup()

        x_cor = data[data.state == answer_state].x.item()
        y_cor = data[data.state == answer_state].y.item()

        tim.goto(int(x_cor), int(y_cor))
        tim.write(answer_state)

# screen.mainloop()