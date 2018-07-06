
# Convert Feet to Inches
# 29 June 2018
# CTI-110 P5T2_FeetToInches 
# Steven Siddall

# Constant for the number of inchest per foot.
INCHES_PER_FOOT = 12
# Main function
def main():
    #Get a number of feet from the user.
    feet = int(input('Enter a number of feet:'))

    #Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
#the feet_to_inches function converts feet to inches
def feet_to_inches(feet):
    
    return feet * INCHES_PER_FOOT

# Call the main function.
main()



