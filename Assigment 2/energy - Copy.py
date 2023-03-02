# energy.py

# A program that calculates the energy after the user has input
# the value for m and c
# Jing Yeh
# Date: 23 February 2023

def energy():
    '''
    This function calcuates the value of energy using 
    Einstein's E = mc^2\    
    '''
    mass = eval(input("Enter the value of m: "))
    speed = eval(input("\nEnter the value of c: "))
    return f"\nThe value of energy, E, is: {mass * speed**2}"

print(energy())