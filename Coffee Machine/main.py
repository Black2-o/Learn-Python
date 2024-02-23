MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 10000,
    "milk": 5000,
    "coffee": 1000,
    "money":0,
}


def waterBack(water, userChose):
    waterNeed = MENU[userChose]["ingredients"]["water"]
    water -= waterNeed
    return water


def coffeeBack(coffee, userChose):
    coffeeNeed = MENU[userChose]["ingredients"]["coffee"]
    coffee -= coffeeNeed
    return coffee


def milkBack(milk, userChose):
    milkNeed = MENU[userChose]["ingredients"]["milk"]
    milk -= milkNeed
    return milk


def allBack(water, coffee, milk, userChose,money):
    # For Report and minimize the value of resources.........
    water = waterBack(water, userChose)
    coffee = coffeeBack(coffee, userChose)
    milk = milkBack(milk, userChose)
    money += MENU[userChose]["cost"]
    resources["water"] = water
    resources["milk"] = milk
    resources["coffee"] = coffee
    resources["money"] = money
    return resources


# For Coffie dibo na dibo nah...........
def coffeDiboorDibonah(userChose,water,milk,coffee):
    if water > MENU[userChose]["ingredients"]["water"]:
        if milk > MENU[userChose]["ingredients"]["milk"]:
            if coffee > MENU[userChose]["ingredients"]["coffee"]:
                return f"Here is your {userChose} ☕️. Enjoy!"
            else:
                return "Sorry there is not enough coffee."
        else:
            return "Sorry there is not enough milk."
    else:
        return "Sorry there is not enough water."


# For Dolar dise thik moto nah nai.
def costNeededAndReturn(userChose):
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    totalGive = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    returnMoney = round((totalGive - MENU[userChose]["cost"]), 2)
    return returnMoney


def coffeeMachine(userChose):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    coffeeVar = coffeDiboorDibonah(userChose,water,milk,coffee)
    if coffeeVar == f"Here is your {userChose} ☕️. Enjoy!":
        returnMoney = costNeededAndReturn(userChose)
        if returnMoney >= 0:
            print(f"Here is your ${returnMoney} in change.")
            print(coffeeVar)
            allBack(water, coffee, milk, userChose, money)
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print(coffeeVar)



# Actual Games goes here
runMachine = True
while runMachine != False:
    userChose: str = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if userChose == "off":
        runMachine = False
    elif userChose == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')

    else:
        coffeeMachine(userChose)
