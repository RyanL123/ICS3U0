#-----------------------------------------------------------------------------
# Name:        Exercise 4
# Purpose:     Display my understanding of for and while loops
#
# Author:      767571
# Created:     Oct-15-2019
# Updated:     Oct-15-2019
#-----------------------------------------------------------------------------

sum = 0
while True:
    a = int(input())
    if a == -1:
        break
    sum += a

for i in range(sum):
    print("*"*i)