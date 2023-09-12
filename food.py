from turtle import Turtle
from random import randint


class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.shape("circle")
        self.turtlesize(0.5, 0.5)
        self.speed(0)
        self.goto(randint(-280, 280), randint(-280, 280))

    def new_pos(self):
        self.goto(randint(-280, 280), randint(-280, 280))
