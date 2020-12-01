import time
from turtle import Screen
from player import Player
from car_manager import CarManager, COLORS
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")

# car manager
car_manager = CarManager()

scorboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # move cars
    car_manager.create_car()
    car_manager.move_cars()

    #  Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scorboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scorboard.increase_level()

screen.exitonclick()
