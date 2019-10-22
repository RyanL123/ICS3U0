#-----------------------------------------------------------------------------
# Name:        Exercise 6
# Purpose:     Display my understanding of functions
#
# Author:      767571
# Created:     Oct-22-19
# Updated:     Oct-22-19
#-----------------------------------------------------------------------------


def convertCToF(temperature):
    if -100 <= temperature <= 100:
        return int(temperature * (9/5)) + 32
    return 'Unacceptable input values.'


def convertFToC(temperature):
    if -100 <= temperature <= 100:
        return int(temperature-32) * (5/9)
    return 'Unacceptable input values.'


def hypotenuse(a, b):
    if a <= 0 or b <= 0:
        return 'Unacceptable input values.'
    return float((a**2 + b**2)**(0.5))


def milesToKm(distance):
    if distance > 0:
        return float(round(distance*1.60934, 2))
    return 'Unacceptable input values.'
