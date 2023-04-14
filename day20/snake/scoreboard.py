from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

with open("high_score.txt") as file:
    high_score = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.high_score = int(high_score)
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
