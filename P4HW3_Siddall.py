# CTI-110 
# P4HW3 - Factoral 
# Steven Siddall 
# 26 June 2018

integer = int( input('Enter a number:'))
while integer < 1:
    integer = int( input('Enter a NonNegative number:'))
factorial = 1
for Number in range(1, integer + 1):
    factorial = factorial * Number
print()
print(' The factorial of', integer, 'is', factorial)
