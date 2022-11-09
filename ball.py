import turtle
from turtle import Turtle

import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(10)


    # def bounce(self):
    #     if self.xcor() > 0:
    #         self.goto(-280, random.randint(-280, 280))
    #     elif self.xcor() <= 0:
    #         self.goto(280, random.randint(-280, 280))

    def move(self):
        self.forward(5)


    def bounce_left(self):
        #self.goto(-280, random.randint(-280, 280))
        self.setheading(random.randint(91, 269))
        self.move()


    def bounce_right(self):
        #self.goto(280, random.randint(-280, 280))
        heading = [random.randint(0, 89), random.randint(271, 360)]
        self.setheading(random.choice(heading))
        self.move()


    def bounce_top(self):
        if self.heading() > 90 and self.heading() < 270:
            self.setheading(random.randint(181,220))
            self.move()


        elif self.heading() < 90 and self.heading() >= 0:
            self.setheading(random.randint(291,359))
            self.move()


        elif self.heading() > 270 and self.heading() < 360:
            self.setheading(random.randint(291, 359))
            self.move()






    def bounce_bottom(self):
        if self.heading() > 90 and self.heading() < 270:
            self.setheading(random.randint(110, 181))
            self.move()

        elif self.heading() < 90 and self.heading() >= 0:
            self.setheading(random.randint(1, 89))
            self.move()

        elif self.heading() > 270 and self.heading() < 360:
            self.setheading(random.randint(1, 89))
            self.move()



    def reset(self):
        self.goto(0,0)
        self.move()


