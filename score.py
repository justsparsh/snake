from turtle import Turtle


class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.points = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.draw_it()

    def draw_it(self):
        self.write(f"Score = {self.points}", align="center", font=("Oswald", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Oswald", 20, "normal"))
