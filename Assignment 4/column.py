# column.py
# A program that prints out every 7th number in the range n to n+41
# Jing Yeh
# 9 March 2023

number = int(input("Enter a number:\n"))
current_number = number
# The incrementor

while current_number in range(number, number + 41):
    # Use while loop instead of for to increase the incrementor by 7
    if  len(str(current_number)) == 1:
        space = " "
    else: 
        space = ""
    print(space, current_number, sep="")
    current_number += 7
    