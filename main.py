import turtle
import time
import player
import car_manager
import scoreboard
import gameover

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)

player = player.Player()
car = car_manager.CarManager()
score = scoreboard.ScoreBoard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.make_cars()
    car.move()

    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            game = gameover.GameOver()

    if player.ycor() == 280:
        score.point()
        player.reset_position()
        car.speed_up()

screen.exitonclick()
