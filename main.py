from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))

ball = Ball()

screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")

screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
speed = .1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    ball.move()
    screen.update()

    # Detect collision with border
    if ball.ycor() > 289 or ball.ycor() < -289:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed *=.8

    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        ball.restart()

    elif ball.xcor() < -380:
        scoreboard.increase_right_score()
        ball.restart()

screen.exitonclick()