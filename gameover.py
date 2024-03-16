import turtle


class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.write("Game Over!", False, "center", ("Arial", 24, "normal"))
