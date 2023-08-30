# This program will take a user input of an
#  angle as a radian and convert it to degrees

# 'degree' variable is set equal to 57.2958
degree = 57.2958

# Setting the variable 'radian' equal to the users input
radian = input("\nWelcome, Please input a radian: ")

# Casting the input from str to float variable
radian = float(radian)

# Multiplying 'degree' by 'radian' to convert radians to degrees
conversion = degree * radian

# Printing float variable 'conversion'
print("\nThe converted radian in degrees is: " + str(conversion))
print("\n")
