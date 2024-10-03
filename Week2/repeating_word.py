print("Please enter a phrase: ")
phrase = input()
length, iteration = len(phrase), 0

while iteration < length:
    iteration += 1
    print(f"Beep{iteration}", end=" ")
