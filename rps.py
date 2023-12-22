def menu():
    
    while True:

        print("-" * 32)
        print(f"|           1. Play            |")
        print(f"|       2. Session Stats       |")
        print(f"|           3. Quit            |")
        print("-" * 32)

        choice = int(input("> "))

        wins = 0
        games = 0
        l = 0
        tie = 0
    
        if wins != 0 and games != 0:
            winp = (wins / games) * 100


        if choice == 1:
            result = play()
    

        elif choice == 2:
            print("Stats for this session :\n")
            print(f"Games = {games}\nWins = {wins}\nLooses = {l}\nTies = {tie}\n\n")

            if wins == 0 and games == 0:
                print("Win % = 0")

            else:
                print(f"Win % = {winp}")


        elif choice == 3:
            return
    
        else:
            return


def play():
    print("a")


