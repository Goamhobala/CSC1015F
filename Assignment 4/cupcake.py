#cupcake.py
# A program that helps me to decide whether to eat the food or not
# Jing Yeh
# 7th March 2023

print('''
Welcome to the 30 Second Rule Expert
------------------------------------
Answer the following questions by selecting from among the options.''', sep="")

def eat():
    '''To print out the result of assesment: Eat'''
    print("Decision: Eat it.")

def do_not_eat():
    '''To print out the result of assesment: Don't eat'''
    print("Decision: Don't eat it.")

def your_call():
    '''To print out the result of assesment: Your call'''
    print("Decision: Your call.")

def licked_by_cat():
    '''When the snack has been licked by a cat'''
    if input("Did the cat lick it? (yes/no)\n") == "yes":
        if input("Is your cat healthy? (yes/no)\n") == "yes":
            eat()
        else:
            your_call()
    else: 
        eat() 

    
if input("Did anyone see you? (yes/no)\n") == "yes":
    if input("Was it a boss/lover/parent? (yes/no)\n") == "yes":
        if input("Was it expensive? (yes/no)\n") == "yes":
            if input("Can you cut off the part that touched the floor? (yes/no)\n") == "yes":
                eat()
            else: 
                your_call()
        else:
            if input("Is it chocolate? (yes/no)\n") == "yes":
                eat()
            else:
                do_not_eat()
    else: 
        eat()
else:
    if input("Was it sticky? (yes/no)\n") == "yes":
        if input("Is it a raw steak? (yes/no)\n") == "yes":
            if input("Are you a puma? (yes/no)\n") == "yes":
                eat()
            else:
                do_not_eat()
        else:
            licked_by_cat()
    else: 
        if input("Is it an Emausaurus? (yes/no)\n") == "yes":
            if input("Are you a Megalosaurus? (yes/no)\n") == "yes":
                eat()
            else:
                do_not_eat()    
        else:
            licked_by_cat()
