from turtle import Turtle

class Dash_line(Turtle):
    def __init__(self):
        super().__init__()

        self.color("red")
        self.draw_line()

    def draw_line(self):
        self.penup()
        self.speed(10)
        self.goto((0, 300))
        self.hideturtle()
        self.right(90)
        for dots in range(60):
            self.penup()
            self.forward(10)
            self.dot()
            self.penup()

class Scoreboard(Turtle):

    def __init__(self,player_select):
        super().__init__()
        self.score = 0
        self.penup()
        if player_select == 1:
            self.goto((-100, 230))
        else:
            self.goto((100, 230))
        self.hideturtle()
        self.write(f'{self.score}', font=('Arial', 30, 'normal'))

    def update_score(self):
        self.score += 1








