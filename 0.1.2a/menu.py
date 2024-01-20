"""
 ________  ________  ________  ________  ________  _________  ________           _____ ______   _______   ________   ___  ___           _____      ________       _______  ________     
|\   __  \|\   ____\|\   __  \|\   ____\|\   __  \|\___   ___\\   ____\         |\   _ \  _   \|\  ___ \ |\   ___  \|\  \|\  \         / __  \    |\   __  \     /  ___  \|\   __  \    
\ \  \|\  \ \  \___|\ \  \|\ /\ \  \___|\ \  \|\  \|___ \  \_\ \  \___|_        \ \  \\\__\ \  \ \   __/|\ \  \\ \  \ \  \\\  \       |\/_|\  \   \ \  \|\  \   /__/|_/  /\ \  \|\  \   
 \ \   ____\ \  \    \ \   __  \ \  \    \ \   __  \   \ \  \ \ \_____  \        \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \ \  \\\  \      \|/ \ \  \   \ \  \\\  \  |__|//  / /\ \   __  \  
  \ \  \___|\ \  \____\ \  \|\  \ \  \____\ \  \ \  \   \ \  \ \|____|\  \        \ \  \    \ \  \ \  \_|\ \ \  \\ \  \ \  \\\  \          \ \  \ __\ \  \\\  \ ___ /  /_/__\ \  \ \  \ 
   \ \__\    \ \_______\ \_______\ \_______\ \__\ \__\   \ \__\  ____\_\  \        \ \__\    \ \__\ \_______\ \__\\ \__\ \_______\          \ \__\\__\ \_______\\__\\________\ \__\ \__\
    \|__|     \|_______|\|_______|\|_______|\|__|\|__|    \|__| |\_________\        \|__|     \|__|\|_______|\|__| \|__|\|_______|           \|__\|__|\|_______\|__|\|_______|\|__|\|__|
                                                                \|_________|                                                                                                            
"""

from os import system, name
import time
import random
import PySimpleGUI as sg
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
    try:
        clear()
        number = float(input("Enter a number: "))
        result = math.sqrt(number)
        print(f"Square root of {number} is {result}")
        select()
    except ValueError:
        print("Please enter a valid number.")
    
def select():
    print("\n Pick your Selection")
    print("[r] Find the Square root of a number")
    print("[b] Back to menu")
    print("[q] Exit")
    user_input = input().strip().lower()
    if user_input == 'r':
        select2()
    elif user_input == 'b':
        clear()
        backtomenu()
        menu()
    elif user_input == 'q':
        clear()
        exit()

def select2():
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
        menu()
    elif user_input == 'q':
        clear()
        exit()

def gui():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
    [sg.Text('Some text on Row 1')],
    [sg.Text('Enter something on Row 2'), sg.InputText(key='input_field')],
    [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Back to menu')]  # Use sg.Button() for 'Back to menu'
    ]

    # Create the Window
    window = sg.Window('Window Title', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        quit()

    elif event == 'Back to menu':
        window.close()  # Close the current window
        menu()

    input_text = values['input_field']  # Access the input value using its key
    if input_text.strip() == '':  # Check if input is empty
        sg.popup('Please Enter Something')
    else:
        sg.popup('You entered: ' + input_text)

    window.close()


def menu():

    clear()
    print("   ___    ___    ___               _    _                                         ")  
    print("  / _ \  / __\  / __\  ___   __ _ | |_ ( ) ___       /\/\    ___  _ __   _   _    ")
    print(" / /_ / / /    /__\// / __| / _` || __||/ / __|     /    \  / _ \| '_ \ | | | |   ")
    print("/ ___/ / /___ / \/  \| (__ | (_| || |_    \__ \    / /\/\ \|  __/| | | || |_| |   ")
    print("\/     \____/ \_____/ \___| \__,_| \__|   |___/    \/    \/ \___||_| |_| \__,_|   ")
    print("Note: This is Version 1.0.2a, there might be bugs still in this, if you experience bugs submit them to "issues" on github ")
    print("\nPick your Selection")
    print("[1] Number Comparison")
    print("[2] Square Root")
    print("[3] GUI Test")
    print("[9] Exit")
    user_input = input().strip().lower()
    if user_input == '1':
        load()
        display_comparison()
    
    elif user_input == '2':
        load()
        select()

    elif user_input == '3':
        load()
        gui()

    elif user_input == '9':
        clear()
        exit()
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
menu()

