from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


#create our snake body my way...
# positions = [-20,0,20]
# turtles = []
# for position in range(0, 3):
#     new_turtle = Turtle(shape = "square")
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(x = positions[position], y = 0)
#     turtles.append(new_turtle)

# #create our snake body
# starting_positions = [(0,0),(-20,0),(-40,0)]
#
# segments = []
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.penup()
#     new_segment.color("white")
#     new_segment.goto(position)
#     segments.append(new_segment)

#create our snake body
snake = Snake()
#creating the object of the food class
food = Food()
# showing scoreboard
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # #code to make the turtle follow the first turtle...
    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num -1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)
    # segments[0].left(90)

    #moving the snake
    snake.move()


    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #detect collision with tail
    #if head collides with any segment in the tail:
    #trigger the game_over
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) <10:
            game_is_on = False
            score.game_over()


















screen.exitonclick()
