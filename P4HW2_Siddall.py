# CTI-110 
# P4HW2 - Running Total 
# Steven Siddall 
# 24 June 2018

total = 0
# Asks the user to enter a number
# Tells user that entering -1 will quit the program
Number = float(input('Enter first number or -1 to quit:'))
# Creates a loop that adds all numbers together that are greater than -1
while Number > -1:
    total = total + Number
# repeats the loop until the user enters -1
    Number = float(input('Enter next number or -1 to quit:'))
#prints a blank line to seperate question and answer
print()
#prints the total of all numbers entered with exception to the negative number
print('Total', total)
