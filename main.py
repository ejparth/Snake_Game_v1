from turtle import Screen
from food import Food
from snake import Snake
from Scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
# Screen animation delay is 0


screen.tracer(0)
game_on = False  # for the while loop

snaky = Snake()
foody = Food()
sb = Score()

screen.listen()
screen.onkey(snaky.up, "Up")
screen.onkey(snaky.down, "Down")
screen.onkey(snaky.right, "Right")
screen.onkey(snaky.left, "Left")

while not game_on:
    screen.update()
    time.sleep(0.1)
    snaky.move()

    if snaky.head.distance(foody) <= 15:
        foody.refresh()
        sb.score_increase()
        snaky.tail()

    if snaky.head.xcor() > 280 or snaky.head.xcor() < -280 or snaky.head.ycor() > 280 or snaky.head.ycor() < -280:
        game_on = True
        sb.gameover()

    # to check whether the head touched the tail
    # Game over
    # but don't check the first head

    for parts in snaky.segments[1:]:
        if snaky.head.distance(parts) < 10:
            game_on = True
            sb.gameover()


screen.exitonclick()
