from machine import MENU, resources, CHANGE

money = 0


def coffee_machine():
    start_selection = True
    while start_selection:
        wantcoffee = input("What would you like to purchase? Espresso - $1.50, Latte - $2.50, or Cappuccino - $3.00?: ")
        global money
        if wantcoffee.lower() == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}g")
            print(f"${'{:.2f}'.format(money)}")
            coffee_machine()
        
        elif wantcoffee.lower() == "off":
            money = 0
            quit()

        selection = MENU[wantcoffee.lower()]
        cost = selection["cost"]
        print(cost)
        water = selection["ingredients"]["water"]
        
        if wantcoffee.lower() != "espresso":
            milk = selection["ingredients"]["milk"]
            
        coffee = selection["ingredients"]["coffee"]

        take_money = True
        while take_money:
            print(f"Please insert the correct change - ${cost}0")
            quarter = float(input("How many quarters?: "))
            dime = float(input("How many dimes?: "))
            nickle = float(input("How many nickles?: "))
            penny = float(input("How many pennies?: "))
            subtotal = (quarter * CHANGE["quarter"]) + (dime * CHANGE["dime"]) + (nickle * CHANGE["nickle"] + (penny * CHANGE["penny"]))
            total_change = subtotal
            
            if wantcoffee.lower() != "espresso":    
                if resources["water"] < selection["ingredients"]["water"] or resources["milk"] < selection["ingredients"]["milk"] or resources["coffee"] < selection["ingredients"]["coffee"]:
                    print("Sorry, not enough resources.")
                    take_money = False
                elif total_change < cost:
                    print("Not enough change. Money refunded.")
                    take_money = False
                elif total_change >= cost:
                    resources["water"] -= water
                    if wantcoffee.lower() != "espresso":
                        resources["milk"] -= milk
                    resources["coffee"] -= coffee
                    money += cost
                    give_back = "{:.2f}".format(total_change - cost)
                    
                    print(f"Here is your ${give_back} in change.")
                    print(f"Here is your {wantcoffee}! Enjoy!")
                    take_money = False
            else:    
                if resources["water"] < selection["ingredients"]["water"] or resources["coffee"] < selection["ingredients"]["coffee"]:
                    print("Sorry, not enough resources.")
                    take_money = False
                elif total_change < cost:
                    print("Not enough change. Money refunded.")
                    take_money = False
                elif total_change >= cost:
                    resources["water"] -= water
                    if wantcoffee.lower() != "espresso":
                        resources["milk"] -= milk
                    resources["coffee"] -= coffee
                    money += cost
                    give_back = "{:.2f}".format(total_change - cost)
                    
                    print(f"Here is your ${give_back} in change.")
                    print(f"Here is your {wantcoffee}! Enjoy!")
                    take_money = False


coffee_machine()
