import random

print("How many live electric cables must I avoid?")
live_cables = int(input())
cables_count = 0

while cables_count < live_cables:
    is_live_cable = random.choice([True, False])

    if not is_live_cable:
        print("Found dead electric cable.")
        continue

    print("Avoided live electric cable.")
    cables_count += 1

print("Finished avoiding live electric cables.")

