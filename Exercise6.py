#-----------------------------------------------------------------------------
# Name:        Exercise 6
# Purpose:     Display my understanding of functions
#
# Author:      767571
# Created:     Oct-21-19
# Updated:     Oct-21-19
#-----------------------------------------------------------------------------


def convertCToF(temperature):
    if -100 <= temperature <= 100:
        return int(temperature * (9/5)) + 32


def convertFToC(temperature):
    if -100 <= temperature <= 100:
        return int(temperature-32) * (5/9)


def hypotenuse(a, b):
    return float((a**2 + b**2)**1/2)


def milesToKm(distance):
    if distance > 0:
        return float(round(distance*1.609, 2))
