from basic_operations import add


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
    print("Please enter the first number:", end="")
    first_number, valid = input_float()
    if not valid:
        return
    print("Please enter the second number:", end="")
    second_number, valid = input_float()
    if not valid:
        return
    return add(first_number, second_number)


MENU_OPTIONS = ["Addition", "Quit"]
MENU_FUNCTIONS = [add_menu]


def run_menu():
    print("Please select one of the operation below.")
    for i, option in enumerate(MENU_OPTIONS):
        print(f"{i + 1}. {option}")

    option, valid = input_option()
    if valid:
        if option == 2:
            return False
        MENU_FUNCTIONS[option - 1]()

    return True


def start_menu():
    print("Welcome to the CMD Calculator!")
    while run_menu():
        pass
