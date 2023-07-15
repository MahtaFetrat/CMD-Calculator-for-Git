import math


def run_back():
    return False


def print_answer(answer):
    print("\n**********")
    print(answer)
    print("**********\n")


def run_sin():
    print("Enter a number in Radians to calculate Sin, * to go back.")
    number = input()
    if number == "*":
        return True
    try:
        number = float(number)
        print_answer(math.sin(number))
        name = input('Enter your name to see new feature')
        print(f'Hello {name}!!! Happy calculating sin!!!')
        return True
    except:
        run_sin()


def run_cos():
    print("Enter a number in Radians to calculate Cosine, * to go back.")
    number = input()
    if number == "*":
        return True
    try:
        number = float(number)
        print_answer(math.cos(number))
        return True
    except:
        run_cos()


def run_tan():
    print("Enter a number in Radians to calculate Tangente, * to go back.")
    number = input()
    if number == "*":
        return True
    try:
        number = float(number)
        print_answer(math.tan(number))
        return True
    except:
        run_tan()


def run_cot():
    print("Enter a number in Radians to calculate Cotangente, * to go back.")
    number = input()
    if number == "*":
        return True
    try:
        number = float(number)
        print_answer(math.cot(number))
        return True
    except:
        run_cot()


def deg_2_rad():
    print("Enter a number in Degrees to calculate Radians, * to go back.")
    number = input()
    if number == "*":
        return True
    try:
        number = float(number)
        print_answer(number * math.pi / 180)
        return True
    except:
        deg_2_rad()


def rad_2_deg():
    print("Enter a number in Radians to calculate Degrees, * to go back.")
    number = input()
    if number == "*":
        return True
    try:
        number = float(number)
        print_answer(number * 180 / math.pi)
        return True
    except:
        rad_2_deg()


operations = [
    ("Sin", run_sin),
    ("Cos", run_cos),
    ("Tan", run_tan),
    ("Cot", run_cot),
    ("Deg to Rad", deg_2_rad),
    ("Rad to Deg", rad_2_deg),
    ("Back", run_back),
]


def run_trigonometric_menu():
    print("Welcome to trigonometric calculator. Choose an operation.")
    for i, operation in enumerate(operations):
        print(f"{i+1}.", operation[0])
    command = input()
    right_command = False
    for i, operation in enumerate(operations):
        if command == str(i + 1):
            right_command = True
            if operation[1]():
                run_trigonometric_menu()
            else:
                return
    if not right_command:
        print("Wrong command!")
        run_trigonometric_menu()
