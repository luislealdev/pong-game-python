from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

left_paddle = Paddle((350,0))
right_paddle = Paddle((-350,0))

ball = Ball()

screen.onkey(left_paddle.up,"Up")
screen.onkey(left_paddle.down,"Down")

screen.onkey(right_paddle.up,"w")
screen.onkey(right_paddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    if ball.ycor() > 289:
        ball.change_direction()

screen.exitonclick()