from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mr Snake")
# Turn off turtle animation
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard= Scoreboard()
# Intial random food
food.refresh
scoreboard

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  # Update screen outside of for loop
  screen.update()
  # Slow down speed
  time.sleep(0.1)
  snake.move()

  # Detect collisions with food by measuring distance from head to food
  if snake.head.distance(food) < 15:
    # Move food to a new location
    food.refresh()
    # Extend snake when it touches food
    snake.extend()
    scoreboard.increase_score()

  # Detect collisions with the wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()

  # Detect collisions with tail
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()
      

  
screen.exitonclick()
