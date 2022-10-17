from turtle import Turtle
import random

colour = ['red', 'blue', 'green', 'orange', 'pink']
MOVE = 10


class Cars:
    def __init__(self):
        self.car_list = []
        self.init_move = MOVE

    def car_creator(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            car.shape('square')
            car.color(random.choice(colour))
            car.shapesize(1, 2)
            new_y = random.randint(-280, 280)
            car.goto(500, new_y)
            self.car_list.append(car)

    def car_move(self):
        for car in self.car_list:
            car.backward(self.init_move)

    def increase_speed(self):
        self.init_move += MOVE






