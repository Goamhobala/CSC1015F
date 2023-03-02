# spam.py
# A program to generate personalised spam message
# Jing Yeh 
# 1st March 2023

def spam(first_name, last_name, country, amount):
    return (f'''
\nDearest {first_name}
It is with a heavy heart that I inform you of the death of my father,
General Fayk {last_name}, your long lost relative from Mapsfostol.
My father left the sum of {amount}USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in {country}.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - {round(amount * 0.3, 1)}USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank {last_name}
''')
    
    
def get_info():
    victim = {}
    victim["first_name"] = input("Enter first name: ")
    victim["last_name"] = input("\nEnter last name: ")
    victim["amount"] = eval(input("\nEnter sum of money in USD: "))
    victim["country"] = input("\nEnter country name: ")
    
    return victim

def main():
    victim = get_info()
    print(spam(victim["first_name"], victim["last_name"], victim["country"], victim["amount"]))
    
if __name__ == "__main__":
    main()