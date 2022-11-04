import turtle
from turtle import Screen, Turtle
from scoreboard import Dash_line, Scoreboard
from  ball import Ball
from paddles import Paddle

# CHANGE BALL MOVE TO HEADING 

screen = Screen()
screen.bgcolor('white')


player1score = Scoreboard(1)
player2score = Scoreboard(2)
player1 = Paddle(1)
player2 = Paddle(2)
#line = Dash_line()
ball = Ball()



def start_game():
    return True


turtle.listen()
screen.onkeypress(player1.move_up, "w")
screen.onkeypress(player1.move_down, "s")
screen.onkeypress(player2.move_up, "Up")
screen.onkeypress(player2.move_down, "Down")
#screen.onkeypress(keep_playing, "space")
# screen.onkeypress(end_game(), "e")

game_is_on = True

while game_is_on:
    ball.move()
    if ball.xcor() == -270 and player1.head.ycor() == ball.ycor():
        ball.bounce_right()
    elif ball.xcor() == 270 and player2.head.ycor() == ball.ycor():
        ball.bounce_left()
    elif ball.xcor() == -280:
        player1score.update_score()
        ball.reset()
        game_is_on = False


    elif ball.xcor() == 280:
        player2score.update_score()
        ball.reset()
        game_is_on = False

















screen.exitonclick()


