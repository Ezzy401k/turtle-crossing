import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE  # Corrected the attribute name

    def make_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.turtlesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y = random.randint(a=-250, b=250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
