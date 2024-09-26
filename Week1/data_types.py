#Display data types.

display_name = "Diagnostics"
model_number = "BOT-X1"
shield = 100
laser_range = 3.5
rocket_range = 75.0

print("#" * 31)
print("#", display_name, ": \t\t\t  #")
print("#", "-" * 27, "#")
print("# Model Number: \t", model_number,  "  #")
print("# Shield (%): \t\t", shield,  "\t  #")
print("# Laser Range (m): \t", laser_range,  "\t  #")
print("# Rocket Range (m): ", rocket_range,  "\t  #")
print("#" * 31, "\n")

print("The data type of model number is ", type(model_number))
print("The data type of shield is ", type(shield))
print("The data type of laser range is ", type(laser_range))
print("The data type of rocket range is ", type(rocket_range))