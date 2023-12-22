def spo_terminal():
    print("-" * 14)
    print("| SPO TERMINAL |")
    print("-" * 14)

    while True:
        command = input("> ")

        command = command.lower()

        if command == "?" or command == "help" or command == "?help" or command == "/?":
            print("Here is the help terminal ... If you have any questions about a command just put (?) before a command, for example ?help")
            #print("")

        elif command == "spo" or command == "?spo":
            print("SPO, for Simplified Python Os is a command line open source os entirely in python")
            print("You can follow the project on Github")
            print("https://github.com/itsal3xis/SPO")

        elif command == "quit":
            return
        
        elif command == "?quit":
            print("This command return back to the main menu")
        
        
        else:
            print("Command unknown... try again or help /?")

        print("\n")
