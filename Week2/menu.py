import random

print("What would you like to see?")
is_valid_option = False

while not is_valid_option:
    print("[1] Random Number")
    print("[2] Random Word")

    print("Please enter your selection:")
    option = input()
    
    if not option.isdigit():
        print("Please select a valid option")
        continue

    option = int(option)

    if option == 1 or option == 2:
        is_valid_option = True

    if option == 1:
        number = random.randint(1, 100)
        print(f"Random number is {number}")
    elif option == 2:
        word = random.choice(["red", "blue", "green", "black", "white"])
        print(f"Random word is {word}")
    else:
        print("Please select a valid option")
