from os import system, name
import math
import time

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def square_root():
    try:
        clear()
        number = float(input("Enter a number: "))
        result = math.sqrt(number)
        print(f"Square root of {number} is {result}")
    except ValueError:
        print("Please enter a valid number.")

def exit():
    print("Exiting", end='', flush=True)
    for i in range(6):
        print(".", end='', flush=True)
        time.sleep(0.5)
        if (i + 1) % 3 == 0:
            print("\b\b\b   \b\b\b", end='', flush=True)
            time.sleep(0.5)
            print("\rExiting", end='', flush=True)
    clear()
    quit
    
def backtomenu():
    print("Exiting Back to the Menu", end='', flush=True)
    for i in range(6):
        print(".", end='', flush=True)
        time.sleep(0.5)
        if (i + 1) % 3 == 0:
            print("\b\b\b   \b\b\b", end='', flush=True)
            time.sleep(0.5)
            print("\rExiting Back to the Menu", end='', flush=True)
    clear()
    import menu
    menu

def select():
    square_root()
    print("\n Pick your Selection")
    print("[r] Find the Square root of a number again")
    print("[b] Back to menu")
    print("[q] Exit")
    user_input = input().strip().lower()
    if user_input == 'r':
        square_root()
    elif user_input == 'b':
        clear()
        backtomenu()
        import menu
        menu
    elif user_input == 'q':
        clear()
        exit()
