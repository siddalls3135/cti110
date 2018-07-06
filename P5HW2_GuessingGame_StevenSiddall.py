# Guessing Game
# 05 JUL 2018
# CTI-110 P5HW2 - Random Number Guessing Game
# Steven Siddall

# Gives access to the random module
import random

# Defines what Random_Number is and gives a range of 1 to 100
# for the program to choose form
def Random_Number():
    randomNumber = random.randint(1, 100)
    return randomNumber

 # Asks user to input a guessed number and returns one of the messages
 #stored on lines 24 - 30
 
def User_Number(message = "What number am I thinking of?: "):
    userNumber = int(input( message ))
    return userNumber

# Returns a message after the user enters a number based on the number the 
# user entered
def Verify_Number(userNumber, randomNumber):
    if userNumber > randomNumber:
        return "Too high try again"
    elif userNumber < randomNumber:
        return "Too low try again"
    else:
        return "Congratulations!"
    
# Adds a play again option for the user
def play_again():
    while True:
        play_again = input("Play again?(y/n) > ")
        if play_again == "y":
            game()
        if play_again == "n":
            exit()
        else:
            print("invalid input")
# Name and start point of the game
def game():
    # Tells program that the start of the game the user isnt congratulated 
    # so "Start" is true and the game starts    
    userCongratulated = False
    Start = True
    game = "game"
    print(game)
    
    # Program chooses a random number, asks the user to guess a number
    # and verifies if the number is high, low or equal to and sends a 
    # message to the user based on those arguements
    while Start:
        randomNumber = Random_Number()
        userNumber = User_Number()
        message = Verify_Number( userNumber, randomNumber)
        
        # Sends a message to user based on user guess
        while message != "Congratulations!":
            # Tells user if they are high, low or right on their guess
            print(message)
            userNumber = User_Number("Try again:")
            message = Verify_Number( userNumber, randomNumber)
        # Prints the message Try again too high, too low or
        # congratulations based off of user guess
        print(message)
        # Adds a space between message and play again option
        print()
        #Runs the play again option as defined in line 33
        play_again()
               
            
game()
