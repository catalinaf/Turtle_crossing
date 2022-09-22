from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
HEADING = 180
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            y_position = random.randint(-250, 280)
            car = Turtle()
            car.pu()
            car.shape("square")
            car.turtlesize(1, 2)
            car.color(random.choice(COLORS))
            car.setheading(HEADING)
            car.goto(310, y_position)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
