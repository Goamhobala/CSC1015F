
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
* 

```python
y = 777
z = lol
print("x", y, "\n", z, end="8==D", sep="-")
'''
output: x-777-
-z8==D
'''
#NOTE: \n is a string, it's just invisible because all it does is to skip a line.
#      However, it is still separated by the separator
```

### Input

-   Always return a string
    
-   use eval() to run the string parsed to it (DON’T use this in real world applications, the last thing you want is to give user control over things that they shouldn’t have control over)
    
    ```python
    height = input("What is your height: ")
    eval(height)
    
    if height < 180:
        print("you fucking midget lol lol lol lol lol lol lol lol")
        for i in range(10):
            print("lmao")
    ```

### Implicit Conversions:

* e.g. integer to float
* If there's a type mismatch, the narrower range value is promoted up
	e.g. int => float
```python
print(5 + 6.0)
```
* Cannot automatically convert down: i.e. Floats do not become int automatically

### Explicit Conversions:

* Typecast methods cast a value to another type

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
print(math.floor(4.9))
# Output: 4
print(round(4.9), round(4.1))
# Output: 5, 4
```

### Module

* A collections of useful functions in modules

* Two ways of importing modules: 
```python
# To import the entire module
import math
print(math.sqrt(4))
```
```python
# To import a certain function or class inside the module
from math import sqrt
print(sqrt(4))
```