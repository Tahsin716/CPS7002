print("What level of brightness is required?: ")
level = int(input())

for i in range(2, level + 1, 2):
    brightness = '*' * i
    print(f"Brightness level: {brightness}")

print("\nAdjustments complete!\n")