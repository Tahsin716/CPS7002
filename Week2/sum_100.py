print("Calculating the sum of the first 100 integers...")
current_sum, current_num = 0, 1

while current_num <= 100:
    current_sum += current_num
    current_num += 1

print(f'Done! The answer is {current_sum}')
