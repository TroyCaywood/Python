import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.car_move()
    car_manager.create_car()

    # Level up
    if player.ycor() > 280:
        scoreboard.increase_score()
        player.goto(0, -280)
        car_manager.increase_speed()
    # Game Over
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
