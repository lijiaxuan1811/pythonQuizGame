"""
Created By: William Li
Created On: 2024-Nov-08
Modified By: William Li
Modified On: 2024-Nov-08
Purpose: This program is a quiz game with 5 questions covering different topics. The user would be asked to
input the answer of each question and the program would output how many questions he answered correctly.
"""
correctAnswers = ["a", "b", "d", "c", "b"] # Stores the correct answers in order for each question
correctQuestions = 0 # Stores the number of questions the user answered right
def checkInput(character):
    # This function returns if the string is a valid input (only contains one letter that is either a, b, c or d)
    return (len(character) == 1) and (character in "abcdABCD")
def answerInput(questionNumber):
    # This function deals with the input and verification of answers for each question
    while True:
        # Continue on and on unless the input is valid
        currentAnswer = input("Your choice: ")
        currentAnswer = currentAnswer.strip().lower() # Remove the spaces and make it lowercase
        if currentAnswer == correctAnswers[questionNumber - 1]: # If the input is the same as the correct answer
            print("Hooray! Your answer is right for this question!\n")
            global correctQuestions
            correctQuestions += 1 # Add 1 to the number of correctly answered questions
            break # Exit the loop
        else:
            # The input is not the same as the correct answer
            if checkInput(currentAnswer): # If the answer is valid
                print("Oops, but your answer is incorrect for this question.\n")
                # Exit without adding marks
                break
            else:
                # Invalid answer
                print("No…no! Could only be a letter a, b, c or d! Please try again!")
print("""Hello! Thank you for taking the time to participate in this fun quiz game!
This game has 5 questions in total about different topics.
Are you ready? Let's go!\n""")
print("""Q1: Which of the following Q-codes in radio communication means "who is calling me"?
(a) QRZ
(b) QTH
(c) QSK
(d) QUA""")
answerInput(1) # Call the function to deal with the input for the first question
print("""Q2: What common animal do the coats of arms of Canada, Belgium, United Kingdom, Singapore, Sri Lanka and India share?
(a) Tiger
(b) Lion
(c) Eagle
(d) Horse""")
answerInput(2)
print("""Q3: What is the northernmost settlement in Canada?
(a) Dawson, YT
(b) Hay River, NT
(c) Iqaluit, NU
(d) Alert, NU""")
answerInput(3)
print("""Q4: For about how long was the development process of the video game Minecraft before it was officially released?
(a) half a year
(b) one year
(c) two years
(d) five years""")
answerInput(4)
print("""Q5: Where was the Windows XP built-in background "Autumn", which features maple leaves falling on the ground taken by the photographer in 1996?
(a) Burlington, Vermont, U.S.A.
(b) Burlington, Ontario, Canada
(c) Algonquin Provincial Park, Ontario, Canada
(d) Augusta, Maine, U.S.A.""")
answerInput(5)
correctPercentage = correctQuestions / 5 # Calculate the correction rate
print(f"Whoosh! The game is up! You answered {correctQuestions} correctly out of the 5 questions, and your correct answer rate is {correctPercentage:.2%}! Well done!")