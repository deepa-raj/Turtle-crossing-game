# TODO 1: Move the turtle with keypress
# TODO 2: Create and move the cars
# TODO 3: Detect collision with car
# TODO 4: Detect when turtle reaches the other side
# TODO 5: Create a scoreboard

import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# turtle = Turtle()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
            # print("GAME OVER")

    # Detect successful crossing
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()




screen.exitonclick()