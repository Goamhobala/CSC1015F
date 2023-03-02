# secret.py

# Program to guess a secret number
# Huleman Suleman
# 10 February 2011

secret_number = 42  # Create secret number in program
guess = 0   # Variable to store user's guess

# As long as we have not found the secret number
while guess != secret_number:
    # get a nuew guess from user
    guess = eval(input("? "))
    # check if guess is too low
    if guess < secret_number:
        print("lo")
    # or too high
    elif guess > secret_number:
        print("hi")
        
print("Correct!")

