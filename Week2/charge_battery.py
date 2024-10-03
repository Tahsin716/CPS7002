print("How many bars should be charged?")
bars = int(input())
bars_charged = 0

while bars_charged < bars:
    bars_charged += 1
    battery_level = ""

    for i in range(bars_charged):
        battery_level += "\U0001F50B"

    print("Charging:", battery_level)

print("The battery is fully charged.")
