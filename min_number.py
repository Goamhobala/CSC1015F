# min_number.py
def min_number(numbers):
    current_number = numbers[0]
    for number in numbers:
        if number > current_number:
            current_number = number
    
    return current_number

def adding_numbers():
    numbers = []
    while True:
        try: 
            number_add = input("Add a number (leave blank to finish adding): ")
            if number_add:
                numbers.append(float(number_add))
            else:
                return numbers
        except ValueError:
            print("Please input a number")



print(min_number(adding_numbers()))
