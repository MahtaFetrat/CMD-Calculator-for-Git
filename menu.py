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



MENU_OPTIONS = ["Trigonometric operations","Quit"]
MENU_FUNCTIONS = [run_trigonometric_menu]


def run_menu():
    print("Please select one of the operation below you may see new features.")
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
