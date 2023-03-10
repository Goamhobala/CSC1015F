# perfect.py
# A program to find all the proper divisors of a number and then
# determine whether it's a perfect number.
# Jing Yeh
# 8 March 2023


number = int(input("Enter a number:\n"))
divisors = ""
perfect = 0
for i in range(1 , number):
    if number % i == 0:
        if i != 1:
            # So that all proper divisors are separated by a single space
            divisors += " "
        divisors = divisors + str(i)
        perfect += i

if perfect == number:
    result = f"{number} is a perfect number."
else:
    result = f"{number} is not a perfect number."

print(
f'''The proper divisors of {number} are:
{divisors}

{result}           
''')



