import colorgram
from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()


tim.shape("turtle")
tim.color("chartreuse4")
tim.speed(10)

colorgram_colors = colorgram.extract('hirst.webp', 10)
colors = []
y_position = 0
tim.sety(y_position)
for color in colorgram_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors.append(new_color)

for i in range(0, 11):
    for j in range(0, 11):
        random_color = choice(colors)
        print(random_color)
        tim.dot(20, random_color)
        tim.forward(50)
    tim.sety(y_position + 50)


screen = Screen()
screen.exitonclick()
