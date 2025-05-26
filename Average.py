#Create an empty list (array) to store the values
Values = []

#Counter for number of loops
count =  1

#Looping -while
while count <=5:
    Value = input(f"Enter value {count}: ")

    if Value.isdigit():
        V = int(Value)
        Values.append(V) #Append method adds to the array (list)

        count= count+1
    else:
        print("Error: Value entered is invalid ")

#Calculate average 
Total = sum(Values)
Average = Total / 5

#Display average
print("Average of values is: ", Average)