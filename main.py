
from data import MENU
from data import resources
from art import logo

profit = 0


def process_coins():
    #print("Please insert coins")
    total = int(input("how many quarters?: ")) - 0.25
    total += int(input("how many dimes?: ")) - 0.1
    total += int(input("how many nickles?: ")) - 0.05
    total += int(input("how many pennies?: ")) - 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_espresso():
    cost = MENU["espresso"]["cost"]
    water = MENU["espresso"]["ingredients"]["water"]
    coffee = MENU["espresso"]["ingredients"]["coffee"]
    enough_water = check_resources("water", water)
    if not enough_water:
        print("Sorry there is not enough water.")
        return 0
    enough_coffee = check_resources("coffee", coffee)
    if not enough_coffee:
        print("Sorry there is not enough coffee.")
        return 0

    print(f"Please pay: ${cost}")
    payment = process_coins()
    if is_transaction_successful(payment, cost):
        resources["water"] -= water
        resources["coffee"] -= coffee
        print("here is your espresso")


def make_latte():
    cost = MENU["latte"]["cost"]
    water = MENU["latte"]["ingredients"]["water"]
    milk = MENU["latte"]["ingredients"]["milk"]
    coffee = MENU["latte"]["ingredients"]["coffee"]
    enough_water = check_resources("water", water)
    if not enough_water:
        print("Sorry there is not enough water.")
        return 0
    enough_milk = check_resources("milk", milk)
    if not enough_milk:
        print("Sorry there is not enough milk.")
        return 0
    enough_coffee = check_resources("coffee", coffee)
    if not enough_coffee:
        print("Sorry there is not enough coffee.")
        return 0
    print(f"Please pay: ${cost}")
    payment = process_coins()
    if is_transaction_successful(payment, cost):
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        print("here is your latte ð")


def make_cappuccino():
    cost = MENU["cappuccino"]["cost"]
    water = MENU["cappuccino"]["ingredients"]["water"]
    milk = MENU["cappuccino"]["ingredients"]["milk"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    enough_water = check_resources("water", water)
    if not enough_water:
        print("Sorry there is not enough water.")
        return 0
    enough_milk = check_resources("milk", milk)
    if not enough_milk:
        print("Sorry there is not enough milk.")
        return 0
    enough_coffee = check_resources("coffee", coffee)
    if not enough_coffee:
        print("Sorry there is not enough coffee.")
        return 0
    print(f"Please pay: ${cost}")
    payment = process_coins()
    if is_transaction_successful(payment, cost):
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        print("here is your cappuccino ð")


def run_report(money):
    print("Available Resources:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(resource, required):
    available = resources[resource]
    if available < required:
        return False
    else:
        return True


def make_coffee():
    print(logo)
    money = 0
    is_on = True
    while is_on:
        request = input("What would you like? (espresso/latte/cappuccino): ")

        if request == "espresso":
            make_espresso()
        elif request == "latte":
            make_latte()
        elif request == "cappuccino":
            make_cappuccino()
        elif request == "off":
            print("Coffee Machine is turned off.")
            is_on = False
            return
        elif request == "report":
            run_report(money)
        else:
            return


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_coffee()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
