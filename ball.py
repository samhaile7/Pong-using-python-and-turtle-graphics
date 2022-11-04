import turtle
from turtle import Turtle

import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(1)


    # def bounce(self):
    #     if self.xcor() > 0:
    #         self.goto(-280, random.randint(-280, 280))
    #     elif self.xcor() <= 0:
    #         self.goto(280, random.randint(-280, 280))

    def move(self):
        self.forward(10)


    def bounce_left(self):
        self.goto(-280, random.randint(-280, 280))

    def bounce_right(self):
        self.goto(280, random.randint(-280, 280))

    def reset(self):
        self.goto(0,0)
        self.move()


