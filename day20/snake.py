from turtle import Turtle
import time

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_body.append(new_segment)

    def move_snake(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_head.forward(move_distance)

    def up(self):
        if self.snake_head.heading() != down:
            self.snake_head.setheading(up)

    def down(self):
        if self.snake_head.heading() != up:
            self.snake_head.setheading(down)

    def left(self):
        if self.snake_head.heading() != right:
            self.snake_head.setheading(left)

    def right(self):
        if self.snake_head.heading() != left:
            self.snake_head.setheading(right)
