from turtle import Screen, Turtle
from scoreboard import Dash_line, Scoreboard
from  ball import Ball
from paddles import Paddle


screen = Screen()
screen.bgcolor('white')


player1score = Scoreboard(1)
player2score = Scoreboard(2)
player1 = Paddle(1)
player2 = Paddle(2)
line = Dash_line()
ball = Ball()
player1.move_up()







screen.exitonclick()


