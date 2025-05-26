#Enter number of days
no_of_days = input("Enter number of days: ")

#Calculation of no. of seconds in no. of days 
if no_of_days.isdigit():
    D = int(no_of_days)
    sec = D*24*60*60

    print(f"{D} days = {sec} seconds")

else:
    print("Number entered is invalid")
