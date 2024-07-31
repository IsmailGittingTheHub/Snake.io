from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

loop = True
while loop:
    screen.update()
    time.sleep(0.1)

    snake.move()
    score.score_board()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score += 1
        score.refresh()


    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.refresh()
        score.reset()
        snake.reset()
        score.refresh()

    # Detect collision with tail.
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.refresh()
            score.reset()
            snake.reset()
            score.refresh()


screen.exitonclick()
