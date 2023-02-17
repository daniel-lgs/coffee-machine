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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_money = 0
machine_is_on = True


def asking_user():
    answer = ""
    secrets_keyword = ["off", "report"]
    while answer not in MENU and answer not in secrets_keyword:
        answer = input("What would you like? (espresso/latte/cappuccino):").lower()
    return answer


def enough_resources(user_order):
    insufficient_resources = []
    for key in MENU[user_order]["ingredients"]:
        if resources[key] < MENU[user_order]["ingredients"][key]:
            insufficient_resources.append(key)
    if len(insufficient_resources) == 0:
        return True
    else:
        print(f"Sorry! There is not enough: {', '.join(insufficient_resources)}.")
        return False


def correct_payment(user_order):
    global machine_money
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    user_payment = quarters + dimes + nickles + pennies
    user_payment = float('{:.2f}'.format(user_payment))
    if user_payment == MENU[user_order]["cost"]:
        machine_money += MENU[user_order]["cost"]
        return True
    elif user_payment > MENU[user_order]["cost"]:
        user_change = user_payment - MENU[user_order]["cost"]
        user_change = float('{:.2f}'.format(user_change))
        print(f"Here is ${user_change} in change.")
        machine_money += MENU[user_order]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_order):
    global resources
    for key in MENU[user_order]["ingredients"]:
        resources[key] -= MENU[user_order]["ingredients"][key]
    print(f"Here is your {user_order} ☕️. Enjoy!")


while machine_is_on:
    user_answer = asking_user()
    if user_answer == "off":
        break
    elif user_answer == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${machine_money}")
    else:
        order = user_answer
        if enough_resources(order):
            if correct_payment(order):
                make_coffee(order)
