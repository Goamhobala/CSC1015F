# printmonth.py
month = input("Enter the name of a month (e.g. January, ..., December):\n")
start_day = input("Enter the start day (1 for Monday, ..., 7 for Sunday):\n"))
def right_justify(number_str):
    if len(number_str) == 1:
        number_str = " " + number_str
    return number_str

thirty_one = ["January", "March","May", "July", "August", "October", "December"]
thirty = ["April", "June", "September", "November"]
twenty_eight = ["February"]

if month in thirty_one:
    day_in_month = 31
elif month in thirty:
    day_in_month = 30
elif month in twenty_eight:
    day_in_month = 28
else:
    day_in_month = False
    
if not day_in_month or start_day not in range(1,8):
    print("Invalid calendar: you have either entered an incorrect month name or start day.")
