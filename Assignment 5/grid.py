# grid.py
def right_justify(number_str):
    if len(number_str) == 1:
        number_str = " " + number_str
    return number_str

def number_grid(start_number):
    char_count = 0
    while char_count <= 41:
        if (char_count + 1) % 7 == 0:
            end_behaviour = "\n"
        
        else:
            end_behaviour = " "
        print(right_justify(str(start_number + char_count)), end=end_behaviour)
        char_count += 1
    
number = int(input("Enter a number between -6 and 2: \n"))
if number > - 6 and number < 2:
    number_grid(number)
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")
            
    