import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        random_chance = random.randint(1,6) #This random number is used to generate the less car
        if random_chance == 1:
            new_car = Turtle()
            new_car.setheading(180)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.forward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT



