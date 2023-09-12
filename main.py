from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

outline = Turtle()
outline.hideturtle()
outline.color("white")
outline.penup()
outline.goto(-300, 300)
outline.pendown()
for i in range(0, 4):
    outline.forward(600)
    outline.right(90)


snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
time.sleep(1)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.new_pos()
        snake.increase_length()
        score.points += 1
        score.clear()
        score.draw_it()
    if snake.snake_head.xcor() > 295 or snake.snake_head.xcor() < -295 or snake.snake_head.ycor() > 295 or snake.snake_head.ycor() < -295:
        game_is_on = False
        score.game_over()

    for seg_num in range(len(snake.segments) - 1, 0, -1):
        if snake.snake_head.distance(snake.segments[seg_num]) < 15:
            game_is_on = False
            score.game_over()

screen.exitonclick()
