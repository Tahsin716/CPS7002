import random

print("How many live electric cables must I avoid?")
live_cables = int(input())
cables_count = 0

while True:
    is_live_cable = random.choice([True, False])

    if is_live_cable:
        print("Avoided live electric cable.")
        cables_count += 1

    if cables_count == live_cables:
        break

print("Finished avoiding live cables.")
