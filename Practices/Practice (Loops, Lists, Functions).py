#-----------------------------------------------------------------------------
# Name:        Practice (Loops, Lists, Functions)
# Purpose:     Practice the use of loops, lists, and functions
#
# Author:      767571
# Created:     Nov-22-19
# Updated:     Nov-22-19
#-----------------------------------------------------------------------------


def get_subject_average(subject, amount_of_marks):
    subject_marks = []
    for i in range(amount_of_marks):
        subject_marks.append(int(input("Enter your mark for the #%i %s test: " % (i+1, subject))))
    if amount_of_marks == 0:
        return 0
    return sum(subject_marks)/amount_of_marks


math_avg = get_subject_average("Math", int(input("How many math marks do you want to enter?")))
english_avg = get_subject_average("English", int(input("How many english marks do you want to enter?")))
science_avg = get_subject_average("Science", int(input("How many science marks do you want to enter?")))
art_avg = get_subject_average("Art", int(input("How many art marks do you want to enter?")))

semester_average = (math_avg+english_avg+science_avg+art_avg)/4

print("Your total average for the semester was: %i" % semester_average)
