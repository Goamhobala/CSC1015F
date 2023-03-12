
### Compiler v.s. Interpreter

-   **Compile**r converts the entire program at once. It scans the entire program and turn it into assembly language which is then translated into binary code. e.g. C++
-   **Interpreter** translates the program in a line by line manner. e.g. Python

### What is a program?

-   A set of unambiguous instruction. (given to a computer)
    e.g. The direction to your house you wrote down for your friend
    
-   Every program contains instructions that the executor understand
-   Written in precise language
    

### Programs and algorithms

-   **Algorithms** is the recipe. It contains the essence of the solution, with all executor-specific details removed.
    
    -   Algorithms are independent of language and computer.
		**Formal**: A sequence of unambiguous instructions for solving a problem.

    -   Doesn’t require implementation in software
    
    -   Not an answer, but the method to get to the answer.
    
    **Elements of Algorithms**
    
    -   **Sequence**: Each step is followed by another step
        
    -   **Selection:** A choice may be made amongst alternatives
        
    -   **Iteration**: A set of steps may be repeated
        
        Note: Any language with these 3 elements can express any classical algorithm
        

### Print
*  A built in function that displays(prints) the given value onto the screen
* "end" and "sep" are **keyword arguments** that change the end of each argument (by default \n which changes a line) and the separator (which separates arguments) between each argument
  (by default is a space)
```python
y = 777
z = "lol"
print("1. ", y, "\n", z)
'''
output:

1. 777
lol
'''
print("2. ", y, "\n", z, end="???", sep="-")
'''
output:

2.-777-
-lol???
'''
# NOTE: \n is a string (similar to an empty string), it's just invisible because all it
# does is to skip a line. However, it is still separated by the separator
```

### Input
*  A built in function that allows you to get a string from the user
-  Always return a string    
-  Use eval() to convert a string into an integer or floating point number (DON’T use this in real world applications, the last thing you want is to give user control over things that they shouldn’t have control over)
    
    ```python
    height = eval(input("What is your height: "))
    
    if height < 183:
        print("You're under 6 foot")
    else:
	    print("You're over 6 foot tall! ")
    ```

### Implicit Conversions:

* e.g. integer to float
* If there's a type mismatch, the narrower range value is promoted up
	e.g. int => float
```python
print(5 + 6.0)
# Output: 11.0
```
* Cannot automatically convert down: i.e. Floats do not become ints automatically

### Explicit Conversions:

* Typecast methods cast a value to another type
* "math" is a module(which is a collection of functions) 
```python
import math
print(int(1.24))
# Output: 1
print(int(1.99))
# Output: 1
print(int("9"))
# Output: 9
# Converts an integer string (e.g. "5", but not "Apple" or "5.4") or a floating point
# number (e.g. 5.4) to the largest smaller integer (e.g. int(5.4) -> 5)
print(float(5))
# Output: 5.0
# Converts an integer or a number string (e.g. "5" or "5.4" but not "Banana") to a
# floating point number (i.e. a decimal number)
print(eval("5"))
# Output: 5
print(math.ceil(4.1))
# Output: 5
# Ceil stands for 'ceiling', namely the smallest larger integer
print(math.floor(4.9))
# Output: 4
# floor is the largest smaller integer
print(round(4.9), round(4.1))
# Output: 5, 4
# round of the value like normal math
```

### Module

* A collections of useful functions in modules
* Two ways of importing modules: 
```python
# To import the entire module
import math
print(math.sqrt(4))
# sqrt for square root
```
```python
# To import a certain function or class inside the module
from math import sqrt
print(sqrt(4))
```