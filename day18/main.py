from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()


tim.shape("turtle")
tim.color("chartreuse4")

# for _ in range(10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# for i in range(3, 11):
#     j = i
#     color = ["cyan", "dark olive green", "cornflower blue", "crimson",
#              "medium violet red", "saddle brown", "dark slate blue", "lime green", ]
#     random_color = color[randint(0, len(color)-1)]
#     tim.pencolor(random_color)
#     for j in range(j):
#         tim.right(360 / i)
#         tim.forward(100)
tim.speed(10)
# tim.pensize(10)
# for i in range(500):
#     color = ["cyan", "dark olive green", "cornflower blue", "crimson",
#              "medium violet red", "saddle brown", "dark slate blue", "lime green", ]
#     tim.pencolor(choice(color))
#     direction = randint(1, 4)
#     if direction == 1:
#         tim.forward(20)
#     elif direction == 2:
#         tim.right(90)
#         tim.forward(20)
#     else:
#         tim.left(90)
#         tim.forward(20)
angle = 0
for i in range(100):
    tim.circle(100)
    tim.setheading(angle)
    angle += 5


screen = Screen()
screen.exitonclick()
