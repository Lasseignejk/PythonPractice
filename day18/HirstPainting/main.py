from turtle import Turtle, Screen, colormode
from random import randint, choice

tim = Turtle()


tim.shape("turtle")
tim.color("chartreuse4")
tim.speed(10)
colormode(255)

y_position = 0
x_position = 0
tim.sety(y_position)
colors = [(253, 252, 241), (238, 250, 244), (188, 19, 46), (244, 233, 64), (252, 232, 237),
          (217, 239, 245), (195, 76, 34), (218, 66, 106), (13, 143, 89), (18, 125, 173)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

for i in range(0, 10):
    for j in range(0, 10):
        random_color = choice(colors)
        tim.dot(20, random_color)
        tim.penup()
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = Screen()
screen.exitonclick()
