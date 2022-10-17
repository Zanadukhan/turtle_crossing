from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(x_cor, y_cor)
        self.current_level = 1

    def level_up(self):
        self.clear()
        self.current_level += 1
        self.write(f'Level:{self.current_level}', False, 'left', font=('Courier', 24, 'normal'))
