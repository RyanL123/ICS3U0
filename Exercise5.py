#-----------------------------------------------------------------------------
# Name:        Exercise 5
# Purpose:     Display my understanding of lists and functions related to them
#
# Author:      767571
# Created:     Oct-18-19
# Updated:     Oct-18-19
#-----------------------------------------------------------------------------

# don't touch this list, make your own!
preMadeList = ['5', '8', '6']

l = []

# take input until 0
while True:
    i = input()
    if i == '0':
        break
    l.append(i)
print(l)

# remove elements 4 and last
l.pop(2)
l.pop(-1)
print(l)

# print slices
print(l[0:2])
print(l[3:8])

# sort and print as string
l.sort()
print(''.join(l))

# merge lists and print
newList = l + preMadeList
print(newList)

# check if input exists within newList
element = input()
if element in newList:
    print("YES")

element = input()
if element not in newList:
    print("NOT")

# add ! to the end of each element
for i in range(len(newList)):
    newList[i] += '!'
print(newList)

# create copy and add TEST to original
newCopy = newList.copy()
newList.append('TEST')

# combine into 2d list and print
listCeption = [newList, newCopy]
print(listCeption)
