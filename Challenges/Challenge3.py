# -----------------------------------------------------------------------------
# Name:        Challenge 3
# Purpose:     To challenge myself
#
# Author:      767571
# Created:     Dec-19-19
# Updated:     Dec-19-19
# -----------------------------------------------------------------------------

def addAllNumbers(fileContent):
    '''
    This function adds all the numbers in the file together into a single digit

    Parameters
    ----------
    fileContent: string

    Returns
    -------
    Int
        All the numbers in the file together into a single digit
    '''
    file = open(fileContent, "r")
    fileContent = str(file.readlines())
    total = fileContent.count("0")
    total += fileContent.count("1")
    total += fileContent.count("2")
    total += fileContent.count("3")
    total += fileContent.count("4")
    total += fileContent.count("5")
    total += fileContent.count("6")
    total += fileContent.count("7")
    total += fileContent.count("8")
    total += fileContent.count("9")
    file.close()
    return total


def countVowels(fileContent):
    '''
    This function counts all the vowels in the file and returns a single digit (consider 'y' a consonant).

    Parameters
    ----------
    fileContent: string

    Returns
    -------
    Int
        Amount of vowels in the file
    '''
    file = open(fileContent, "r")
    fileContent = str(file.readlines()).upper()
    total = fileContent.count("A")
    total += fileContent.count("E")
    total += fileContent.count("I")
    total += fileContent.count("O")
    total += fileContent.count("U")
    total += fileContent.count("Y")
    return total


def countConsonants(fileContent):
    '''
    This function does the same as countVowels() except for consonants instead (consider 'y' a consonant).

    Parameters
    ---------
    fileContent: string

    Int
        Amount of consonants in the file
    '''
    file = open(fileContent, "r")
    fileContent = str(file.readlines()).upper()
    vowelsAscii = [65, 69, 73, 79, 85, 89]
    count = 0
    for i in range(len(fileContent)):
        if ord(fileContent[i]) not in vowelsAscii and 65 <= ord(fileContent[i]) <= 90:
            count += 1
    return count

