#Computing Area and Perimeter of a Square using functions

#Function to Calculate Area
def area(x):
    return x*x

#Function to Calculate Perimeter
def perimeter(x):
    return 4*x

#Main function   
def main():
    #Enter a number corresponding to the side length of the square
    length = input("Enter length as: ")

    if length.isdigit():
        x = y = float(length) 

        #Call functions
        A = area(x)
        P = perimeter(x)

        #Display the Area and Perimeter
        print(f"Area = {A}")
        print(f"Perimeter = {P}")
    else:
        print("Invalid entry")

main() 