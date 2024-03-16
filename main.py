import turtle
import time
import player
import car_manager
import scoreboard
import gameover

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)  # Turn off animation

# Create instances of Player, CarManager, ScoreBoard, and GameOver
player = player.Player()  # Create the player object
car = car_manager.CarManager()  # Create the car manager object
score = scoreboard.ScoreBoard()  # Create the scoreboard object

# Listen for keyboard input
screen.listen()
screen.onkey(player.up, "Up")  # When the "Up" key is pressed, call the player's up method

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Introduce a short delay to control the game's speed
    screen.update()  # Update the screen

    car.make_cars()  # Create cars
    car.move()  # Move the cars

    # Check for collisions with cars
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False  # End the game if there's a collision
            game = gameover.GameOver()  # Display game over message

    # Check if the player has reached the finish line
    if player.ycor() == 280:
        score.point()  # Increment the score
        player.reset_position()  # Reset the player's position
        car.speed_up()  # Increase the speed of cars

# Exit the game when the screen is clicked
screen.exitonclick()
