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

game_is_on = True






screen.onkeypress(player1.move_up, "w")
screen.onkeypress(player1.move_down, "s")
screen.onkeypress(player2.move_up, "Up")
screen.onkeypress(player2.move_down, "Down")
#screen.onkeypress(start_game, "j")
screen.listen()
#screen.onkeypress(end_game, "e")




while game_is_on:
    screen.update()
    ball.move()






    if -280 < ball.xcor() < -260 and ball.ycor() <= player1.head.ycor() and ball.ycor() >= player1.tail.ycor(): # DUPLICATE FOR PLKAYER 2
        ball.bounce_right()
        ball.color("blue")

    elif 250 < ball.xcor() < 280 and ball.ycor() <= player2.head.ycor() and ball.ycor() >= player2.tail.ycor():
        ball.bounce_left()
        ball.color("red")



    if -260 < ball.xcor() < 260 and 260 < ball.ycor() < 270:
            ball.bounce_top()

    if -260 < ball.xcor() < 260 and -270 < ball.ycor() < -260:
            ball.bounce_bottom()

    if ball.xcor() < -280:
        player1score.update_score()
        ball.reset()
        if player1score.score == 5:
            game_is_on = False
            player1score.game_over()


    if ball.xcor() > 280:
        player2score.update_score()
        ball.reset()
        if player2score.score == 5:
            game_is_on = False
            player2score.game_over()

    else:
        continue




screen.exitonclick()


