from basic_operations import add, subtract, multiply, divide
from trigonometric import run_trigonometric_menu


def input_option():
    try:
        option = int(input())
        if option not in range(1, len(MENU_OPTIONS) + 1):
            print("Option out of range!")

        return option, True
    except:
        print("Invalid option!")
        return None, False


def input_float():
    try:
        float_number = float(input())
        return float_number, True
    except:
        print("Invalid float input!")
        return None, False


def add_menu():
    print("Please enter the first number:", end=" ")
    first_number, valid = input_float()
    if not valid:
        return
    print("Please enter the second number:", end=" ")
    second_number, valid = input_float()
    if not valid:
        return
    print(f"The response is: {add(first_number, second_number)}")


def subtract_menu():
    print("Please enter the first number:", end=" ")
    first_number, valid = input_float()
    if not valid:
        return
    print("Please enter the second number:", end=" ")
    second_number, valid = input_float()
    if not valid:
        return
    print(f"The response is: {subtract(first_number, second_number)}")


def multiply_menu():
    print("Please enter the first number:", end=" ")
    first_number, valid = input_float()
    if not valid:
        return
    print("Please enter the second number:", end=" ")
    second_number, valid = input_float()
    if not valid:
        return
    print(f"The response is: {multiply(first_number, second_number)}")


def division_menu():
    print("Please enter the first number:", end=" ")
    first_number, valid = input_float()
    if not valid:
        return
    print("Please enter the second number:", end=" ")
    second_number, valid = input_float()
    if not valid:
        return
    if second_number == 0:
        print("Division by zero not possible!")
        return
    print(f"The response is: {divide(first_number, second_number)}")


MENU_OPTIONS = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Trigonometric operations",
    "Quit",
]
MENU_FUNCTIONS = [
    add_menu,
    subtract_menu,
    multiply_menu,
    division_menu,
    run_trigonometric_menu,
]


def run_menu():
    print("Please select one of the operation below you may see new features:")
    for i, option in enumerate(MENU_OPTIONS):
        print(f"{i + 1}. {option}")

    option, valid = input_option()
    if valid:
        if option == len(MENU_OPTIONS):
            return False
        MENU_FUNCTIONS[option - 1]()

    return True


def start_menu():
    print("Welcome to the CMD Calculator!")
    while run_menu():
        pass
