
# Conversion Program
# 01 July 2018
# CTI-110 P5HW1_TestGrades 
# Steven Siddall

# This program converts kilometers to miles.
CONVERSION_FACTOR = 0.6214

# The main functions gets a distance in kilometers and calls
# the show_miles function to convert it.
def main():
    # Get the distance in kilometers
    kilometers = float(input('enter a distance in kilometers:'))
    # Display the distance converted to miles
    show_miles(kilometers)

# The show_miles function converts the parameter to KM from
# kilometers to miles and displays the result
def show_miles(km):
        # Calculate miles
    miles = km * CONVERSION_FACTOR
    
    # Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

# Call the main function.
main()
