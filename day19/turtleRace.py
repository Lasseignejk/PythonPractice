from turtle import Turtle, Screen
import random

is_racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win a race? Enter a color: ")

colors = ["red", "blue", "green", "yellow", "purple"]
y_axis = 90
all_turtles = []

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    y_axis -= 30
    all_turtles.append(new_turtle)

if user_bet:
    is_racing = True

while is_racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The winner is {winning_color}. You won!")
            else:
                print(f"The winner is {winning_color}. You lost.")

        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)


screen.exitonclick()
