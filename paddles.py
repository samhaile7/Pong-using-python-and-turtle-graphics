from ball import Ball
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, player_num):
        super().__init__()
        self.player = player_num
        self.segments = []
        self.start_pos()

    def start_pos(self):
        ycor = 10
        if self.player == 1:
            xcor = -270
        else:
            xcor = 270

        for part in range(10):
            seg1 = Turtle()
            seg1.shape("square")
            seg1.penup()
            seg1.speed(10)
            seg1.goto(xcor,ycor)
            self.segments.append(seg1)
            ycor -= 10

    def move_up(self):

        for seg in self.segments:
            new_y = seg.ycor() + 30
            seg.goto(seg.xcor(), new_y)

    def move_down(self):

        for seg in self.segments:
            new_y = seg.ycor() - 30
            seg.goto(seg.xcor(), new_y)





