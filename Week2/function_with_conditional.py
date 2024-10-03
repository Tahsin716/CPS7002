def identify():
    print("What lies before us?")
    response = input()
    message = "It is time to run!" if response == "a large boulder" else "We will be fine."
    print(message)

identify()