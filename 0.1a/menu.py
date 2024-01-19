from os import system, name
import time

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
    print("Loading", end='', flush=True)
    for i in range(6):
        print(".", end='', flush=True)
        time.sleep(0.5)
        if (i + 1) % 3 == 0:
            print("\b\b\b   \b\b\b", end='', flush=True)
            time.sleep(0.5)
            print("\rLoading", end='', flush=True)
    clear()

def menu():
    user_input = input().strip().lower()
    if user_input == '1':
        clear()
        import compare
        compare
    
    elif user_input == '2':
        load()
        import root
        root

    elif user_input == '3':
        load()
        import gui
        gui

    elif user_input == '9':
        clear()
        exit()
        quit

clear()
print("   ___    ___    ___               _    _                                           _      ___")  
print("  / _ \  / __\  / __\  ___   __ _ | |_ ( ) ___       /\/\    ___  _ __   _   _     / |    / _ \ ")
print(" / /_ / / /    /__\// / __| / _` || __||/ / __|     /    \  / _ \| '_ \ | | | |    | |   | | | |")
print("/ ___/ / /___ / \/  \| (__ | (_| || |_    \__ \    / /\/\ \|  __/| | | || |_| |    | | _ | |_| |")
print("\/     \____/ \_____/ \___| \__,_| \__|   |___/    \/    \/ \___||_| |_| \__,_|    |_|(_) \___/ ")
print("                                                                                                ")
print("Pick your Selection")
print("[1] Number Comparison")
print("[2] Square Root")
print("[3] GUI Test")
print("[9] Exit")
menu()
