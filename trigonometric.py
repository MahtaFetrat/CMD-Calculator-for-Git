import math

def run_back():
    return False

def print_answer(answer):
    print('\n**********')
    print(answer)
    print('**********\n')
    
def run_sin():
    print('Enter a number in Radians, * to go back.')
    number = input()
    if number == '*':
        return True
    try:
        number = float(number)
        print_answer(math.sin(number))
        return True
    except:
        run_sin()

operations = [('Sin',run_sin),('Back',run_back)]

def run_trigonometric_menu():
    print('Welcome to trigonometric calculator. Choose an operation.')
    for i,operation in enumerate(operations):
        print(f'{i+1}.',operation[0])
    command = input()
    right_command = False
    for i,operation in enumerate(operations):
        if command == str(i+1):
            right_command = True
            if operation[1]():
                run_trigonometric_menu()
            else:
                return
    if not right_command:
        print('Wrong command!')
        run_trigonometric_menu()