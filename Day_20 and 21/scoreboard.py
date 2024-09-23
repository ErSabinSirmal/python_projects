from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            my_score = data.read()
        self.high_score = int(my_score)
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.pencolor("white")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align= ALIGNMENT, font=FONT)

    # Used to keep the high score
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.penup()
    #     self.hideturtle()
    #     self.pencolor("white")
    #     self.goto(0,0)
    #     self.write("Game Over!", align = "center", font = ("Arial", 30,"normal"))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()