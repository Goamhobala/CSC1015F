# secret2.py

# Program to guess a secret number
# Huleman Suleman
# 10 February 2011
# Edited by Jing Yeh
# Date: 23 February 2023

secret_number = 42  # Create secret number in program
guess = 0   # Variable to store user's guess

# As long as we have not found the secret number
while guess != secret_number:
    # Get a nuew guess from user
    guess = eval(input("What is the secret number? "))
    # Check if the guess is too low
    if guess < secret_number:
        print("That is way too low. Please try again.")
    # Check if the guess too high
    if guess > secret_number:
        print("That is much too high. Please try again.")
        
print("Congratulations, you have guessed the secret number!")

