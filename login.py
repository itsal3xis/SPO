from random import randint
import time

def login():
    password = "psv1os" #python security version 1 os
    check = randint(10,99)

    print("-" * 23)
    print("| Verify your identity |")
    print("-" * 23)
    
    print("\n\n\n")
    
    print("------")
    print(f"| {check} |")
    print("------")
    check_user = int(input("Write the number > "))
    
    if check_user == 0:
        return #Admin debug


    if check_user == check:
        password_user = input("Write the password > ")
        if password_user == password:
            print("Connecting...")
            time.sleep(3)
    else:
        print("Disconnecting...")
        time.sleep(1)
        quit()

login()