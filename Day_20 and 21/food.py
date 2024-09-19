from turtle import Turtle
import random
# Inherit the functionality of the Turtle class to the Food class....
class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Now the food class able to access the methods of the Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
