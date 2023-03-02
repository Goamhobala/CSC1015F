# time.py
# A program to get the hours, minutes, seconds from the user and then check if they are valid
# Jing Yeh 
# 1st March 2023

def check_time(hours, minutes, seconds):
    '''
    To check if the time data is valid.
    '''
    if hours not in range(0, 24) or minutes not in range(0, 61) or seconds not in range(0, 61):
        return "Your time is invalid."
        
    else: return "Your time is valid."
    
def get_info():
    '''
    To get the time data from the user
    '''
    time = {}
    time["hours"] = int(input("Enter the hours: "))
    time["minutes"] = int(input("Enter the minutes: "))
    time["seconds"] = int(input("Enter the seconds: "))
    return time

def main():
    time = get_info()
    print(check_time(time["hours"], time["minutes"], time['seconds']))

if __name__ == "__main__":
    main()