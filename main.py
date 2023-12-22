from login import login
from terminal import spo_terminal
from rps import menu

game_list = []

while True:
    print("\n\n\n\n\n")
    print("-" * 25)
    print(f"| {' ' * 5}1. Terminal      |")
    print(f"| {' ' * 5}2. Programs      |")
    print(f"| {' ' * 5}3. Settings      |")
    print("-" * 25)

    choice = int(input("> "))

    if choice == 1:
        term = spo_terminal()

        if term == "add rps":
            game_list.append("Rock Paper Scissors")



    elif choice == 2:

        if len(game_list) == 0:
            print("No games installed")
    
        else:
            for el in game_list:
                oc = 1
                print(f"{oc}: {el}")
                oc += 1

            game_choice = int(input("> "))

            if game_choice == 1:
                menu()