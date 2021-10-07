# TODO: Do any required imports first


from data import MENU
from data import resources


def make_espresso():
    return 0


def make_latte():
    return 0


def make_cappuccino():
    return 0


def run_report():
    return 0


def make_coffee():
    # TODO: Prompt user for what they would like (espresso/latte/cappuccino):
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == "espresso":
        make_espresso()
    elif coffee == "latte":
        make_latte()
    elif coffee == "cappuccino:":
        make_cappuccino()
    elif coffee == "off":
        return
    elif coffee == "report:":
        run_report()
    else:
        return

    # TODO: Turn off the coffee machine with secret word

    # TODO: Add print report function

    # TODO: Add check sufficient resources function


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(f"Resources: {resources} \nMenu: {MENU}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
