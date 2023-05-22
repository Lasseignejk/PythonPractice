import turtle 
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def moveState(self,x,y, answer):
        self.goto(x,y)
        self.write(arg=f"{answer}", move=False, align='center', font=('Arial', 8, 'normal'))

states_correct = 0

data = pandas.read_csv("50_states.csv")

states_list = data["state"].to_list()

while states_correct != 50:
    answer_state = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit": 
        break
    if answer_state in states_list: 
        states_correct += 1
        state = data[data.state == answer_state]
        state_on_board = State()
        state_on_board.moveState(x=int(state.x), y=int(state.y), answer=answer_state)
        states_list.remove(answer_state)

state_dict = {
    "states": states_list
}
states_df = pandas.DataFrame(state_dict)
states_df.to_csv("states_to_learn.csv")

        
