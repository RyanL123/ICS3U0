# -----------------------------------------------------------------------------
# Name:        Challenge 1
# Purpose:     To challenge myself
#
# Author:      767571
# Created:     Nov-29-19
# Updated:     Nov-29-19
# -----------------------------------------------------------------------------


def add_two_integers(int1, int2):
    '''
    Calculates the sum of two integers

    Parameters
    ----------
    int1: int
        First integer to be added
    int2: int
        Second integer to be added

    Returns
    -------
    int
        Sum of two integers
    '''
    return int1 + int2


assert add_two_integers(1, 3) == 4, "Expecting sum of 1 and 3 to be 4"


def sub_two_integers(int1, int2):
    '''
    Calculate the difference between two integers

    Parameters
    ----------
    int1:
        Integer to be subtracted from
    int2:
        Integer to be subtracted

    Returns
    -------
    int
        Difference of the two integers
    '''
    return int1 - int2


assert sub_two_integers(4, 3) == 1, "Expecting 4 subtracted by 3 to be 1"


def multiply_two_integers(int1, int2):
    '''
    Calculates the product of two integers

    Parameters
    ----------
    int1: int
        Integer to be multiplied
    int2: int
        Integer to be multiplied

    Returns
    -------
    int
        Product of the two integers
    '''
    return int1 * int2


assert multiply_two_integers(2, 3) == 6, "Expecting product of 2 and 3 to be 6"


def divide_two_integers(int1, int2):
    '''
    Calculates the quotient of two integers

    Parameters
    ----------
    int1: int
        Dividend
    int2: int
        Divisor

    Returns
    -------
    int
        Quotient of the two integers
    '''
    return int1 / int2


assert divide_two_integers(6, 3) == 2, "Expecting 6 divided by 3 to be 2"


def int_div_two_floats(float1, float2):
    '''
    Calculates the integer quotient of two floats

    Parameters
    ----------
    float1: float
        Dividend
    float2: float
        Divisor

    Returns
    -------
    int
        Integer quotient of the two floats
    '''
    return int(float1 // float2)


assert int_div_two_floats(6.0, 5.0) == 1, "Expecting 6.0 integer divided by 5.0 to be 1"


def odd_or_even(integer):
    '''
    Determines if an integer is odd or even

    Parameters
    ----------
    integer: int
        Integer being evaluated

    Returns
    -------
    String
        Whether the integer is odd or even
    '''
    if integer % 2 == 0:
        return "Even"
    return "Odd"


assert odd_or_even(7) == "Odd", "Expecting 7 to be odd"


def count_to_zero(integer):
    '''
    Based on input, count either up or down to zero

    Parameters
    ----------
    integer: int
        Value to start at when counting to 0

    Returns
    -------
    None
    '''
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
    '''
    Calculates the factorial of the given input

    Parameters
    ----------
    integer: int
        The number which the factorial is being calculated for

    Returns
    -------
    int
        The factorial of the integer
    '''
    if integer <= 0 or integer >= 20:
        return "Please enter a positive integer under 20"
    outcome = integer
    while integer != 1:
        outcome *= integer - 1
        integer -= 1
    return outcome


assert factorial(5) == 120, "Expecting 5 factorial to be 120"


def triangle_number(integer):
    '''
    Calculates the triangle number of the given input

    Parameters
    integer: int
        The number which the triangle number is being calculated for

    Returns
    int
        The triangle number of the integer
    '''
    if integer <= 0 or integer >= 20:
        return "Please enter a positive integer under 20"
    outcome = integer
    while integer != 0:
        outcome += integer - 1
        integer -= 1
    return outcome


assert triangle_number(5) == 15, "Expecting the triangle number of 5 to be 15"


user_choice = None

while user_choice != 0:
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
    user_choice = int(input("Choose an option above: "))

    if user_choice == 1:
        print(add_two_integers(int(input("Enter an integer: ")), int(input("Enter an integer: "))))
    elif user_choice == 2:
        print(sub_two_integers(int(input("Enter an integer: ")), int(input("Enter an integer: "))))
    elif user_choice == 3:
        print(multiply_two_integers(int(input("Enter an integer: ")), int(input("Enter an integer: "))))
    elif user_choice == 4:
        print(divide_two_integers(int(input("Enter an integer: ")), int(input("Enter an integer: "))))
    elif user_choice == 5:
        print(int_div_two_floats(float(input("Enter an integer: ")), float(input("Enter an integer: "))))
    elif user_choice == 6:
        print(odd_or_even(int(input("Enter an integer: "))))
    elif user_choice == 7:
        count_to_zero(int(input("Enter an integer: ")))
    elif user_choice == 8:
        print(factorial(int(input("Enter an integer: "))))
    elif user_choice == 9:
        print(triangle_number(int(input("Enter an integer: "))))
