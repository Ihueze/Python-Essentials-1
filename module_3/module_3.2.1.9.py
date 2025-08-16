"""
Objectives
Familiarize the student with:

using the break statement in loops;
reflecting real-life situations in computer code.
Scenario
The break statement is used to exit/terminate a loop.

Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters 
"chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be 
printed to the screen, and the loop should terminate.

Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.

"""
# Solution

# the secret word
secret_word = "chupacabra"

# User should enter a word
user_word = input("Enter a word:")

# looping on till the user enter the right word
while user_word != secret_word:
    print("Enter other word")
    user_word = input("Enter a word:")

# conditional statement
    if user_word == secret_word:
        print("You've successfully left the loop.")
        break
