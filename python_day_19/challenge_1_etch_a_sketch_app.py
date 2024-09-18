from turtle import Turtle, Screen
tim = Turtle()
def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkeypress(key = "w", fun = move_forwards)
screen.onkeypress(key = "a", fun = turn_left)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = clear)




screen.exitonclick()