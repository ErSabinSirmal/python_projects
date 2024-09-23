from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score




screen = Screen()
screen.setup(width = 800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# create the paddle at the two different position
r_paddle = Paddle((350 ,0))
l_paddle = Paddle((-350, 0))

# move the ball
ball = Ball()

#scoreboard
score = Score()
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.goto(350,0)
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce the ball.
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect the ball when  right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        # when right side paddle misses the ball the score of the left side increase
        score.l_point()

    #Detect L paddle misses:
    if ball.xcor() < - 380:
        ball.reset_position()
        # when left side paddle misses the ball the score of the reft side increase
        score.r_point()


screen.exitonclick()