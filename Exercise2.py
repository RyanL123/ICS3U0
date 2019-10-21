#-----------------------------------------------------------------------------
# Name:        Exercise 2
# Purpose:     Display understanding of variables, taking input, string concatenation and typecasting to string
#
# Author:      767571
# Created:     Oct-8-19
# Updated:     Oct-21-19
#-----------------------------------------------------------------------------

PI = 3.14
numberOne = float(input("Please enter a number"))
print("A circle with that radius would have a area of %.2f" %(PI*numberOne**2))
numberTwo = float(input("Please enter another number"))
print("Those numbers converted to integers are: " + str(int(numberOne)) + ", " + str(int(numberTwo)) + "\n")

print("The sum of the two numbers is %i" % (numberOne + numberTwo))
print("The difference of the two numbers is %.2f" % (numberOne - numberTwo))
print("The product of the two numbers is %.2f" % (numberOne*numberTwo))
print("The first number divided by the second number is %.2f" % (numberOne/numberTwo))
print("The second number divided by the first number is %.2f" % (numberTwo/numberOne))
print("The first number divided by the second number as a integer is %i" % (numberOne//numberTwo))
print("The second number divided by the first number as a integer is %i" % (numberTwo//numberOne))
print("The first number modulo the second number is %i" % (numberOne % numberTwo))
print("The second number modulo the first number is %i" % (numberTwo % numberOne))

# 5^2 is first evaluated, which is then used as the divisor of 75
# 10 % 6 is calculated after, leaving only addition and subtraction
# Finally, the operations becomes: 45+3-4 = 44
# Integer division is on the same level as multiplication and division, evaluated from left to right
order_of_operations = 45+75/5**2-10%6

print(order_of_operations)
