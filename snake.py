from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def increase_length(self):
        extra_segment = Turtle("square")
        extra_segment.color("white")
        extra_segment.penup()
        extra_segment.goto(self.segments[-1].pos())
        self.segments.append(extra_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() == 0 or self.snake_head.heading() == 180:
            self.snake_head.setheading(90)

    def left(self):
        if self.snake_head.heading() == 90 or self.snake_head.heading() == 270:
            self.snake_head.setheading(180)

    def down(self):
        if self.snake_head.heading() == 0 or self.snake_head.heading() == 180:
            self.snake_head.setheading(270)

    def right(self):
        if self.snake_head.heading() == 90 or self.snake_head.heading() == 270:
            self.snake_head.setheading(0)
