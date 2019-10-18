#-----------------------------------------------------------------------------
# Name:        Exercise 2
# Purpose:     Display understanding of variables, taking input, string concatenation and typecasting to string
#
# Author:      767571
# Created:     8-Oct-19
# Updated:     8-Oct-19
#-----------------------------------------------------------------------------

PI = 3.14
a = float(input("Please enter a number"))
print("A circle with that radius would have a area of %.2f" %(PI*a**2))
b = float(input("Please enter another number"))
print("Those numbers converted to integers are: " + str(int(a)) + ", " + str(int(b)) + "\n")

print("The sum of the two numbers is %i" % (a + b))
print("The difference of the two numbers is %.2f" % (a - b))
print("The product of the two numbers is %.2f" % (a*b))
print("A divided by B is %.2f" % (a/b))
print("B divided by A is %.2f" % (b/a))
print("A divided by B as a integer is %i" % (a//b))
print("B divided by A as a integer is %i" % (b//a))
print("A modulo B is %i" % (a%b))
print("B modulo A is %i" % (b%a))

# 5^2 is first evaluated, which is then used as the divisor of 75
# 10 % 6 is calculated after, leaving only addition and subtraction
# Finally, the operations becomes: 45+3-4 = 44
order_of_operations = 45+75/5**2-10%6

print(order_of_operations)