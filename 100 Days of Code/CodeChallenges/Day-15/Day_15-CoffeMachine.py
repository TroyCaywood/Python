from machine import MENU

# TODO 1 Prompt user what would you like: Espresso, Latte, or Cappuccino

def coffee_machine():
    money = 0
    inventory = {
        "water": 300,
        "milk": 200,
        "coffee": 100}
    machine_on = True
    while machine_on:
        wantcoffee = input("What would you like to purchase? Espresso, Latte, or Cappuccino?: ")

coffee_machine()

