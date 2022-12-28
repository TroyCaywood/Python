from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_speed = 0.1
        self.hideturtle()
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        # Space out creation of cars by only creating cars if randint picks 1
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS)
            random_y = random.randint(-250, 250)
            # Place car on random Y position
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    # Move cars
    def car_move(self):
        for car in self.all_cars:
            car.moving = car.xcor() - self.car_speed
            car.setposition(car.moving, car.ycor())

    def increase_speed(self):
        self.car_speed += 5
