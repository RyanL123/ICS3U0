#-----------------------------------------------------------------------------
# Name:        Challenge 1
# Purpose:     To challenge myself
#
# Author:      767571
# Created:     Nov-20-19
# Updated:     Nov-21-19
#-----------------------------------------------------------------------------


def add_two_integers():
    int1 = int(input("Enter an integer: "))
    int2 = int(input("Enter an integer: "))
    return int1+int2


def sub_two_integers():
    int1 = int(input("Enter an integer: "))
    int2 = int(input("Enter an integer: "))
    return int1-int2


def multi_two_integers():
    int1 = int(input("Enter an integer: "))
    int2 = int(input("Enter an integer: "))
    return int1*int2


def div_two_integers():
    int1 = int(input("Enter an integer: "))
    int2 = int(input("Enter an integer: "))
    return int1/int2


def int_div_two_floats():
    float1 = float(input("Enter a float: "))
    float2 = float(input("Enter a float: "))
    return float1//float2


def odd_or_even():
    integer = int(input("Enter an integer: "))
    if integer % 2 == 0:
        return "Even"
    return "Odd"


def count_to_zero():
    integer = int(input("Enter an integer: "))
    if integer > 0:
        for i in range(integer, -1, -1):
            print(i)
    elif integer < 0:
        for i in range(integer, 1, 1):
            print(i)
    else:
        print(0)


def factorial(integer):
    if integer <= 0 or integer >= 20:
        return "Please enter a positive integer under 20"
    outcome = integer
    while integer != 1:
        outcome *= integer-1
        integer -= 1
    return outcome


def triangle_number(integer):
    if integer <= 0 or integer >= 20:
        return "Please enter a positive integer under 20"
    outcome = integer
    while integer != 0:
        outcome += integer-1
        integer -= 1
    return outcome


user_choice = None

while user_choice != 0:
    print("Choose an option below:")
    print("1. Add two integers.")
    print("2. Subtract two integers.")
    print("3. Multiply two integers.")
    print("4. Divide two integers.")
    print("5. Perform integer division on two floats.")
    print("6. Odd or even (figure out if the entered value is odd or even).")
    print("7. Count to zero (based on input, count either up or down to zero using a for loop).")
    print("8. Factorial!")
    print("9. nth Triangle Number!")
    print("0. Exit")
    user_choice = int(input())

    if user_choice == 1:
        print(add_two_integers())
    elif user_choice == 2:
        print(sub_two_integers())
    elif user_choice == 3:
        print(multi_two_integers())
    elif user_choice == 4:
        print(div_two_integers())
    elif user_choice == 5:
        print(int_div_two_floats())
    elif user_choice == 6:
        print(odd_or_even())
    elif user_choice == 7:
        count_to_zero()
    elif user_choice == 8:
        print(factorial(int(input("Enter an integer: "))))
    elif user_choice == 9:
        print(triangle_number(int(input("Enter an integer: "))))
