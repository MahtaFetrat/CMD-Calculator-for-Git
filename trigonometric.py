import math

def run_back():
    return False

operations = [('Back',run_back)]

def run_trigonometric_menu():
    print('Welcome to trigonometric calculator. Choose an operation.')
    for i,operation in enumerate(operations):
        print(f'{i+1}.',operation[0])
    command = input()
    for i,operation in enumerate(operations):
        if command == str(i+1):
            if operation[1]():
                run_trigonometric_menu()
            else:
                return
    print('Wrong command!')
    run_trigonometric_menu()