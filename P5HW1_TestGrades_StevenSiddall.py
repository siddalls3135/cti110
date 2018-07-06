# Calculate test scores and return an average of scores
# 30 June 2018
# CTI-110 P5HW1_TestGrades 
# Steven Siddall

# Finds the total of all inputted scores.
# defines how the program will get the average score
def calc_average( score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) /5
    return average

#Defines what the grade is
def determine_grade(score):
    if(score < 60):
        return "F"
    elif(score < 70):
        return "D"
    elif(score <80):
        return "C"
    elif(score <90):
        return "B"
    elif(score < 101):
        return "A"
    # Creates a error message for numbers inputted that have not
    # been assigned a letter grade.
    else:
        return "Error. Not within scoring parameters"

  # Defines scores
  # Asks user to enter a number and returns a letter grade.
def scores():
    score1 = float (input('input score 1:'))
    score2 = float (input('input score 2:'))
    score3 = float (input('input score 3:'))
    score4 = float (input('input score 4:'))
    score5 = float (input('input score 5:'))
    return score1, score2, score3, score4, score5

# Prints results
def Results(score1, score2, score3, score4, score5):
    # Creates a field for number scores and letter grades.
    # prints letter grades for numbers entered.
    # sep = "/n" tells the program to cascade the grade display.
    print('\nScore\tGrade')
    print( str (score1) + "\t" + determine_grade( score1), \
           str (score2) + "\t" + determine_grade( score2), \
           str (score3) + "\t" + determine_grade( score3), \
           str (score4) + "\t" + determine_grade( score4), \
           str (score5) + "\t" + determine_grade( score5), sep = "\n")
    # Creates a space between the score/grade and the average lines
    print()
# Starts the program.
def main():
# Prints the results of your score with a grade and average
        score1, score2, score3, score4, score5 = scores()
        Results(score1, score2, score3, score4, score5)
        print( "Your average is", calc_average(score1, score2, score3, score4, score5))
main()
