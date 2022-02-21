from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
# Screen animation delay is 0


screen.tracer(0)
game_on = False

snaky = Snake()

screen.listen()
screen.onkey(snaky.up, "Up")
screen.onkey(snaky.down, "Down")
screen.onkey(snaky.right, "Right")
screen.onkey(snaky.left, "Left")



while not game_on:
    screen.update()
    time.sleep(0.1)
    snaky.move()

screen.exitonclick()
