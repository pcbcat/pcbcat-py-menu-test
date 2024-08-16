"""Changes:
    Fixed bug where if you would exit it would spit out dots and go back to the menu.
    Fixed bug where if you would go back to menu while in number comp it would exit the whole program.
    got rid of unneeded functions like select() and select2().
    added fake loop with square root.
    added funny easter egg
"""

from os import system, name
import time
import random
import math

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def exit():
    print("Exiting", end='', flush=True)
    for i in range(6):
        print(".", end='', flush=True)
        time.sleep(0.5)
        if (i + 1) % 3 == 0:
            print("\b\b\b   \b\b\b", end='', flush=True)
            time.sleep(0.5)
            print("\rExiting", end='', flush=True)
            break
    clear()
    quit

def load():
    clear()
    print("\n\nLoading", end='', flush=True)
    for i in range(6):
        print(".", end='', flush=True)
        time.sleep(0.5)
        if (i + 1) % 3 == 0:
            print("\b\b\b   \b\b\b", end='', flush=True)
            time.sleep(0.5)
            print("\rLoading", end='', flush=True)
    clear()



def display_comparison():
    clear()
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
    print("Pick your Selection")
    print("[1] Display the comparison again")
    print("[2] Back to menu")
    print("[3] Exit")
    user_input = input().strip().lower()
    if user_input == '1':
        display_comparison()
    
    elif user_input == '2':
        clear()
        backtomenu()
       
    elif user_input == '3':
        clear()
        exit()

def square_root():
    print("Pick your Selection")
    print("[r] Find the Square root of a number")
    print("[b] Back to menu")
    print("[q] Exit")
    user_input = input().strip().lower()
    if user_input == 'r':
        try:
                clear()
                number = float(input("Enter a number: "))
                result = math.sqrt(number)
                print(f"Square root of {number} is {result}")
                print("\n Pick your Selection")
                print("[r] Find the Square root of a number again")
                print("[b] Back to menu")
                print("[q] Exit")
                user_input = input().strip().lower()
                if user_input == 'r':
                    square_rootrpt()
                elif user_input == 'b':
                    clear()
                    backtomenu()
                    menu()
                elif user_input == 'q':
                    clear()
                    exit()
        except ValueError:
                print("Please enter a valid number.")

def square_rootrpt():
    clear()
    number = float(input("Enter a number: "))
    result = math.sqrt(number) 
    print(f"Square root of {number} is {result}")
    print("\n Pick your Selection")
    print("[r] Find the Square root of a number again")
    print("[b] Back to menu")
    print("[q] Exit")
    user_input = input().strip().lower()
    if user_input == 'r':
        square_rootrpt()
    elif user_input == 'b':
        clear()
        backtomenu()
        menu()
    elif user_input == 'q':
        clear()
        exit()

def menu():

    clear()
    print("   ___    ___    ___               _    _                                         ")  
    print("  / _ \  / __\  / __\  ___   __ _ | |_ ( ) ___       /\/\    ___  _ __   _   _    ")
    print(" / /_ / / /    /__\// / __| / _` || __||/ / __|     /    \  / _ \| '_ \ | | | |   ")
    print("/ ___/ / /___ / \/  \| (__ | (_| || |_    \__ \    / /\/\ \|  __/| | | || |_| |   ")
    print("\/     \____/ \_____/ \___| \__,_| \__|   |___/    \/    \/ \___||_| |_| \__,_|   ")
    print("Note: This is Version 1.0.2a, there might be bugs still in this, if you experience bugs submit them to ""issues"" on github ")
    print("\nPick your Selection")
    print("[1] Number Comparison")
    print("[2] Square Root")
    print("[9] Exit")
    user_input = input().strip().lower()
    if user_input == '1':
        load()
        display_comparison()
    
    elif user_input == '2':
        load()
        square_root()

    elif user_input == '9':
        clear()
        exit()
        quit    

    elif user_input == 'sqrt':
        print("hehe squirt")
        time.sleep(1)
        menu()

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
            menu()
            
clear()
menu()

