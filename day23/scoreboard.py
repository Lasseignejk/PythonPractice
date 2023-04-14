from turtle import Turtle
FONT = ("Courier", 24, "normal")

# writes the level we're currently on in the top left side of the screen. Level: 1
# Also controls the Game Over sequence when you are hit by a car.


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.goto(-230, 250)
        self.update_scoreboard()

    def update_scoreboard(self):

        self.write(f"Level {self.current_level}",
                   align="center", font=("Courier", 20, "normal"))

    def level_up(self):
        self.current_level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))
