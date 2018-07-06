# CTI-110 
# P4HW1 - Distance Traveled 
# Steven Siddall 
# 23 June 2018

# Asks the user to enter the vehicles speed
Speed = float( input('Vehicle Speed:'))
# Asks the user to enter the hours the vehicle has traveled
time = int( input('Hours Traveled?:'))
# Prints a blank line to sperate the question and answer
print()
# Prints Hour and Distance with a space between them
print( 'Hour','\t','Distance')
# Creates a loop that allows the user to enter any number.
# time + 1 ensures all numbers entered are multiplied by distance
for Hour in range(1, time + 1):
    distance = Speed * Hour
    print( Hour,'\t',distance)
