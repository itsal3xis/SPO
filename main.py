from login import login
from terminal import spo_terminal

print("\n\n\n\n\n")
print("-" * 25)
print(f"| {' ' * 5}1. Terminal      |")
print(f"| {' ' * 5}2. Games         |")
print(f"| {' ' * 5}3. Settings      |")
print("-" * 25)

choice = int(input("> "))

if choice == 1:
    spo_terminal() 