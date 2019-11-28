#-----------------------------------------------------------------------------
# Name:        Practice (Loops, Lists, Functions)
# Purpose:     Practice the use of loops, lists, and functions
#
# Author:      767571
# Created:     Nov-22-19
# Updated:     Nov-28-19
#-----------------------------------------------------------------------------


def get_subject_average(subject, amount_of_marks):
    subject_total = 0
    # Add mark to total
    for i in range(amount_of_marks):
        subject_total += int(input("Enter your mark for the #%i %s test: " % (i+1, subject)))
    # No marks given for subject
    if amount_of_marks == 0:
        return None
    # Return subject average
    return subject_total/amount_of_marks


semester_total = []

math_avg = get_subject_average("Math", int(input("How many math marks do you want to enter?")))
eng_avg = get_subject_average("English", int(input("How many english marks do you want to enter?")))
sci_avg = get_subject_average("Science", int(input("How many science marks do you want to enter?")))
art_avg = get_subject_average("Art", int(input("How many art marks do you want to enter?")))

# Ignores subjects with no marks given
if math_avg is not None:
    semester_total.append(math_avg)

if eng_avg is not None:
    semester_total.append(eng_avg)

if sci_avg is not None:
    semester_total.append(sci_avg)

if art_avg is not None:
    semester_total.append(art_avg)

# Calculate semester average
semester_average = (sum(semester_total))/len(semester_total)

print("Your total average for the semester was: %i" % semester_average)
