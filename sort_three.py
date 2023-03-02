# sort_three.py
num1 = eval(input("1: "))
num2 = eval(input("2: "))
num3 = eval(input("3: "))


if num2 >= num1:
    if num3 >= num2:
        maximum = num3
        middle = num2
        minimum = num1
    else :
         maximum =  num2
         middle = num1
         minimum = num3
        
else:
    if num2 >= num3:
        maximum = num1
        middle = num2
        minimum = num3
    
    else:
        maximum = num3
        middle = num1
        minimum = num2
        
print(maximum, middle, minimum, sep="-")