from os import system, name
import random
import time


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_comparison():
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    if num1 > num2:
        print("Number one is greater than Number two!")
        print(num1, ">", num2, "\n")
    elif num1 < num2:
        print("Number two is greater than Number one!")
        print(num1, "<", num2, "\n")
    else:
        print("It's a Draw!")
        print(num1, "=", num2, "\n")

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

while True:
    clear()
    display_comparison()
    print("Pick your Selection")
    print("[Enter] Display the comparison again")
    print("[1] Back to menu")
    print("[2] Exit")
    user_input = input().strip().lower()
    if user_input == 'enter':
        continue
    elif user_input == '1':
        clear()
        backtomenu()
        import menu
        menu
    elif user_input == '2':
        clear()
        exit()
