# row.py
'''
Question 3 [25 marks]
Write a program called 'row.py' that asks the user to enter a number, n, where -6<n<93. The
program will print a sequence of 7 numbers, starting from that value.
Each number must be printed using exactly two characters. If the number takes two characters to
print, e.g. 34 or -5, then just print it. If the number takes less than two characters to print, e.g. 0 or 9,
then print a space in front of it.
Numbers must be separated by a single space.
Sample IO (The input from the user is shown in bold font – do not program this):
Enter the start number:
7
7 8 9 10 11 12 13
Sample IO (The input from the user is shown in bold font – do not program this):
Enter the start number:
35
35 36 37 38 39 40 41
Introducing some terminology, we say that the numbers are printed using a field width of 2 and are
right-justified.
'''
# A program that prints out a sequence of 7 numbres
# Jing Yeh
# 9 March 2023

number = int(input("Enter the start number:\n"))
sequence = ""

for i in range(number, number + 7):
    if len(str(i)) == 1:
        sequence += " "
    if i != number:
        # cannot comnbine two if statements as that would only add one space in
        # in front of the single digit numbers
        sequence += " "
    sequence += str(i)
print(sequence)
