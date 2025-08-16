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
