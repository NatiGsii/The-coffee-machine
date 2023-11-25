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
    "water": 400,
    "milk": 260,
    "coffee": 100,
}



def report(choosed):
    if choosed == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        # for n in resources:
        #     print(f"{n}: {resources[n]}")
        print(f"Money: ${new_balance}")
# TODO: 2. Check resource.

def resource_reviser(choosed):
    if choosed == 'espresso':
        resources['water'] -= MENU[choosed]['ingredients']['water']
        resources['coffee'] -= MENU[choosed]['ingredients']['coffee']
    elif choosed != 'report' and choosed != 'off':
        resources['water'] -= MENU[choosed]['ingredients']['water']
        resources['coffee'] -= MENU[choosed]['ingredients']['coffee']
        resources['milk'] -= MENU[choosed]['ingredients']['milk']
    return resources

def resource_checker(choosed):
    up = True
    if choosed == 'espresso':
        if MENU[choosed]['ingredients']['water'] > resources['water']:
            if MENU[choosed]['ingredients']['coffee'] > resources['coffee']:
                print("Sorry there is not enough Water and Coffee.")
                up = False
            else:
                print("Sorry there is not enough Water.")
                up = False
        elif MENU[choosed]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough Coffee.")
            up = False
    elif choosed != 'report' and choosed != 'off':
        if MENU[choosed]['ingredients']['water'] > resources['water']:
            if MENU[choosed]['ingredients']['coffee'] > resources['coffee']:
                if MENU[choosed]['ingredients']['milk'] > resources['milk']:
                    print("Sorry there is not enough Water, Milk, and Coffee.")
                    up = False
                else:
                    print("Sorry there is not enough Water and Coffee.")
                    up = False
            elif MENU[choosed]['ingredients']['milk'] > resources['milk']:
                print("Sorry there is not enough Water and Milk.")
                up = False
            else:
                print("Sorry there is not enough Water.")
                up = False
        elif MENU[choosed]['ingredients']['coffee'] > resources['coffee']:
            if MENU[choosed]['ingredients']['milk'] > resources['milk']:
                print("Sorry there is not enough Coffee and Milk.")
                up = False
            else:
                print("Sorry there is not enough Coffee.")
                up = False
        elif MENU[choosed]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is not enough Milk.")
            up = False
    return up

# TODO: 3. Calculate the amount of coins inserted in dollars
def calculator(quarters, dimes, nickles, pennies):
    money = 0
    money += quarters * 0.25
    money += dimes * 0.10
    money += nickles * 0.05
    money += pennies * 0.01
    return money

def change_calculator(choosed):
    up = True
    if coin_calculator > MENU[choosed]['cost']:
        change = coin_calculator - MENU[choosed]['cost']
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice} ☕. Enjoy!")
    elif coin_calculator < MENU[choosed]['cost']:
        print("Sorry there is not enough money. Money refunded.")
        up = False
    return up




# TODO: 4 Balance sheet.
def balance(choosed):
    balance = 0
    if choosed != 'report' and choosed != 'off':
        balance += MENU[choosed]['cost']
    return balance

# TODO: 1. Ask user to choose a drink.
new_balance = 0
up = True
while up:
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if resource_checker(choice) == True:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            coin_calculator = calculator(quarters, dimes, nickles, pennies)
            if change_calculator(choice) == True:
                resource_reviser(choice)
                new_balance += balance(choice)
    elif choice == 'report':
        report(choice)
    elif choice == 'off':
        up = False












