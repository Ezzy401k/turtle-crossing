import turtle

FONT = ("Courier", 18, "normal")

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the turtle object
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle cursor
        self.score_point = 1  # Initialize the score_point attribute

        # Call the update_score method to display the initial score
        self.update_score()

    def update_score(self):
        # Update the score display
        self.clear()  # Clear previous score before updating
        self.goto(-280, 250)  # Set the position for displaying the "Level" text
        self.write("Level: ", False, font=FONT)  # Display the "Level" text
        self.goto(-190, 250)  # Set the position for displaying the score
        self.write(self.score_point, False, font=FONT)  # Display the current score

    def point(self):
        # Increase the score by 1 and update the score display
        self.score_point += 1  # Increment the score
        self.update_score()  # Update the score display
