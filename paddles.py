from ball import Ball
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, player_num):
        super().__init__()
        self.player = player_num
        self.segments = []
        self.start_pos()
    def start_pos(self):
        if self.player == 1:
            xcor = -270
            ycor = 10
            for part in range(3):
                seg1 = Turtle()
                seg1.goto(xcor,ycor)
                self.segments.append(seg1)
                ycor -= 10
        else:
            xcor = 270
            ycor = 10
            for part in range(3):
                seg1 = Turtle()
                seg1.goto(xcor, ycor)
                self.segments.append(seg1)
                ycor -= 10


