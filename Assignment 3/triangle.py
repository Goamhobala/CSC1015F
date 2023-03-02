# triangle.py
# A program to calculate the area of a triangle constructed by the user
# Jing Yeh
# 2 March 2023

import math

def herons_formula(sides):
    '''
    To calculate the area of a triangle using heron's formula
    '''
    s = 0
    for side in sides:
        s += side
    s /= 2
    
    try:
        return round(math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2])), 2)
        
    except ValueError:
        return False
    
def get_sides():
    '''
    To ask for the three sides of the triangle from the user
    '''
    sides = []
    side_indices = ["first", "second", "third"]    
    for side_index in side_indices:
        sides.append(float(input(f"Enter the length of the {side_index} side: ")))
        
    return sides

def main():
    sides = get_sides()
    area = herons_formula(sides)
    
    if area:
        print(f"The area of the triangle with sides of length {sides[0]} and {sides[1]} and {sides[2]} is {area}.")
    else:
        print("Error: The input does not describe a triangle.")

if __name__ == "__main__":
    main()
    