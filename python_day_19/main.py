from turtle import Turtle, Screen
tim = Turtle()
def move_forwards():
    tim.forward(50)

screen = Screen()
screen.listen() #Set focus on TurtleScreen (in order to collect key-events).
# Dummy arguments are provided in order
# to be able to pass listen() to the onclick method.
screen.onkey(key = "space", fun = move_forwards)
screen.exitonclick()

