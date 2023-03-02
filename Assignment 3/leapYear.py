# leapYear.py
# A program to check if the year input is a leap year
# Jing Yeh 
# 1st March 2023
'''
Question 4 [20 marks]
Write a program called leapYear.py to determine whether a year is a leap year or not. A year is a
leap year if (a) it is divisible by 400 or (b) it is divisible by 4 but not by 100. Your program must accept
input from the user in the form of an integer representing the year. Then, it checks if it is a leap year
or not.
'''
def leap_year_checker():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"\n{year} is a leap year.")
    else:
        print(f"\n{year} is not a leap year.")
        

leap_year_checker()
