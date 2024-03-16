import turtle

class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the turtle object
        self.write("Game Over!", False, "center", ("Arial", 24, "normal"))  # Write "Game Over!" on the screen at the center, using Arial font, size 24, and normal style
