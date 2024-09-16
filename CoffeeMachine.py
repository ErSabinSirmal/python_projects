MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """Return true when order can be made, False if ingredient are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coin inseted"""
    print("please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) *0.1
    total += int(input("how many nickles?: ")) *0.05
    total += int(input("how many pennies?: ")) *0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """returns a true value when payment is accepted, or false if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is {change} in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. Money refunded")
        return False
    


def make_coffee(drink_name,order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy! ")    
     




is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"cost: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]): 
                make_coffee(choice, drink["ingredients"])



