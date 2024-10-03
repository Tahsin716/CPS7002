print("How many rows should I display?: ")
rows = int(input())
print("How many columns should I display?: ")
columns = int(input())

print("Here I go...\n")

for i in range(rows):
    for j in range(columns):
        print("|\U0001F31E|", end='')
    print()

print("\nDone!")
