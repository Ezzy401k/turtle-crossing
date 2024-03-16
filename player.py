import turtle

STARTING_POSITION = (0, -280)  # Initial position of the player
MOVE_DISTANCE = 10  # Distance the player moves in each step
FINISH_LINE_Y = 200  # Y-coordinate of the finish line

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the turtle object
        self.shape("turtle")  # Set the shape of the player to a turtle
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(STARTING_POSITION)  # Move the player to the starting position
        self.setheading(90)  # Set the orientation of the player to face upwards

    def up(self):
        # Move the player upwards by MOVE_DISTANCE units
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        # Reset the player's position to the starting position
        self.goto(STARTING_POSITION)
