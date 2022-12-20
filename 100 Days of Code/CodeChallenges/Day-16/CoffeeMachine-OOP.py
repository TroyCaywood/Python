from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    selected_coffee = input(f"Please make a selection ({options}): ")

    if selected_coffee == "off":
        is_on = False
    elif selected_coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        selection = menu.find_drink(selected_coffee)

    if coffee_maker.is_resource_sufficient(selection) and money_machine.make_payment(selection.cost):
        coffee_maker.make_coffee(selection)
