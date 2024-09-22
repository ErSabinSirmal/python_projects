from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.my_score()

    def my_score(self):
        self.clear()
        self.goto(-260,260)
        self.write(f"Level: {self.level}",font= FONT)

    def update_level(self):
        self.level +=1
        self.my_score()