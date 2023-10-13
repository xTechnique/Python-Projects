import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
car = CarManager()
p1 = Player()
p1


screen.onkeypress(p1.go_up, "Up")
screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(p1) < 20:
            game_is_on = False

    if p1.ycor() > 280:
        p1.next_level()
        car.car_level()



