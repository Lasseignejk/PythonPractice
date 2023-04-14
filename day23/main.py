import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_cars()
    carManager.car_forward()

    for car in carManager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.go_to_start()
        carManager.level_up()
        scoreboard.level_up()

screen.exitonclick()
