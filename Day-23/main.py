import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing Capstone Game")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

# handling the key press
screen.listen()
screen.onkey(player.move_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()

    # Detect collision with car
    for my_car in car.cars:
         if my_car.distance(player) < 20:
             game_is_on = False
             player.game_over()


    # Detect the Player has reached teh other side
    if player.is_at_finish_line():
        # player.update_level()
        # print(f"hello {player.ycor()}")
        player.go_to_start()
        car.level_up()
        score.update_level()






screen.exitonclick()