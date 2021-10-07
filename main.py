
from data import MENU
from data import resources
from art import logo


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
    return cost


def make_latte():
    return 0


def make_cappuccino():
    return 0


def run_report(money):
    print("Available Resources:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


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
