from turtle import Turtle

HOME = (0, -380)


class Player_char(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(HOME)

    def up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def finish(self):
        if self.ycor() == 340:
            self.goto(HOME)
