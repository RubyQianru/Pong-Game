from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

screen.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(.1)
    ball.detect_collide_wall()
    ball.move()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.detect_collide_paddle()
    screen.update()

    # r_paddle miss
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.reverse_move()
        scoreboard.l_point()


    # l_paddle miss
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.reverse_move()
        scoreboard.r_point()


    #detect collision with wall





screen.exitonclick()