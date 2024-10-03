print("What phrase do you see?: ")
word, word_reversed = input(), ""
length = len(word)

print("Reversing...")

for i in range(length - 1, -1, -1):
    word_reversed += word[i]

print(f"The reversed word is: {word_reversed}")