# What is an octothorpe?
# <- This is  an octothorpe.
# What is the octothorpe used for in python?
# Notes, also known in the programming community as Comments.

print("hello world.")
print("howdy, y'all!")
print("I like typing this.")
print("Printing....Yay!!!")

# Practice with Maths and things
print("I will now count my chickens.")
print("Hens", 25 + 30 / 6)
print("Roosters:", 100 - 25 * 3 % 4)
print("Now, I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)

# This is the section I did myself
# Is the area of a 5x6 object larger than the area of a 4x7 object?
print("Is 5 * 6 > 4 * 7 true?")
print(5 * 6 > 4 * 7)
# A floating number determines how many decimals are used in a number
print("%.2f" % 30)
# This would be thirty using floating numbers
# This is all I had to do for this assignment

# variables
cars = 80
space_in_a_car = 4.0
drivers = 30
passengers = 115
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can trasport", carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")

# More variables

myName = "Illian Tear"
myAge = 46
myHeight = 69 # inches
myEyes = "Green"
myTeeth = "White"
myHair = "A lot"

print("Let's talk about %s." % myName)
print("He's %d inches tall." % myHeight)
print("He's got %s eyes and %s hair." % (myEyes, myHair))
print("His teeth \tare usually %s depending \n on the coffee." % myTeeth)
print("if I add %d and %d, I get %d." % (myAge, myHeight, myAge + myHeight))