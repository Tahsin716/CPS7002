print("How far are we from the cave?: ")
steps = int(input())

for i in range(steps, 0, -1):
    print(f"{i} {'steps' if i > 1 else 'step'} remaining")
