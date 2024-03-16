import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the turtle object
        self.hideturtle()  # Hide the turtle cursor
        self.all_cars = []  # List to store all the car objects
        self.speed = STARTING_MOVE_DISTANCE  # Set the initial speed of the cars

    def make_cars(self):
        # Create new cars randomly
        random_chance = random.randint(1, 6)  # Random chance for creating a new car
        if random_chance == 1:  # 1 in 6 chance of creating a car
            new_car = turtle.Turtle()  # Create a new turtle object for the car
            new_car.shape("square")  # Set the shape of the car
            new_car.penup()  # Lift the pen to avoid drawing lines
            new_car.turtlesize(1, 2)  # Set the size of the car
            new_car.color(random.choice(COLORS))  # Set a random color for the car
            new_car.setheading(180)  # Set the initial direction of the car (facing left)
            random_y = random.randint(a=-250, b=250)  # Random y-coordinate within a range
            new_car.goto(300, random_y)  # Set the initial position of the car off-screen on the right
            self.all_cars.append(new_car)  # Add the new car to the list of all cars

    def move(self):
        # Move all cars forward
        for car in self.all_cars:  # Iterate through all cars
            car.forward(self.speed)  # Move the car forward according to its speed

    def speed_up(self):
        # Increase the speed of the cars
        self.speed += MOVE_INCREMENT  # Increase the speed by the move increment
