from turtle import Turtle, Screen
from player_char import Player_char
from car import Cars
import time
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)
screen.title('turtle_crossing')
cars = Cars()
player_char = Player_char()
level = Scoreboard(-400, 350)
level.write(f'Level:{level.current_level}', False, 'left', font=('Courier', 24, 'normal'))



screen.listen()
screen.onkey(player_char.up, 'Up')

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    cars.car_creator()
    cars.car_move()

    for car in cars.car_list:
        if player_char.distance(car) < 25:
            game_on = False
            game_over = Scoreboard(0, 0)
            game_over.write('GAME OVER', False, 'center')

        if player_char.ycor() == 340:
            player_char.goto(0, -380)
            cars.increase_speed()
            level.level_up()















screen.exitonclick()