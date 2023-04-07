from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    # detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -300:
        game_running = False
        scoreboard.game_over()

    # detect collision with tail
    # look at all the segments of the snake body besides the head. slice from index 1 to the end.
    # slice:  array[1:5:1]  start at index 1, stop at 4, increment by 1
    # array[::-1]  reverses the array. slice everything, but increment by -1, so backwards
    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()

screen.exitonclick()
