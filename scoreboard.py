import turtle

FONT = ("Courier", 18, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score_point = 1  # Initialize score_point attribute
        self.update_score()

    def update_score(self):
        self.clear()  # Clear previous score before updating
        self.goto(-280, 250)
        self.write(f"Level: ", False, font=FONT)
        self.goto(-190, 250)
        self.write(self.score_point, False, font=FONT)

    def point(self):
        self.score_point += 1
        self.update_score()