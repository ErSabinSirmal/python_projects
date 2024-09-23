STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()


    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() >FINISH_LINE_Y:
            return True
        else:
            return False
    def go_to_start(self):
        self.goto(0,-280)


    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write("Game over!",align= "center",font=("Arial",24, "normal"))