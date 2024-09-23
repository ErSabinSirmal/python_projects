from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]



    def create_snake(self):
        # create our snake body
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            # new_segment = Turtle("square")
            # new_segment.penup()
            # new_segment.color("white")
            # new_segment.goto(position)
            # self.segments.append(new_segment)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())  #position is the method of turtle class..

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].left(90)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear() # cear the all segments that added
        self.create_snake()
        self.head = self.segments[0]

  #method that used to move the turtle ....
    def up(self):
        if self.head.heading() != DOWN: #this is the condition that is used to restrict the turtle to
            # move opposite direction of the first turtle of head turtle
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




