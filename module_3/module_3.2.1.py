secret_number = 777

print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Ask the user for their first guess
user_number = int(input("Enter a number: "))

# Keep looping until the guess is correct
while user_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Enter a number: "))

# When guess is correct
print("Well done, muggle! You are free now.")
