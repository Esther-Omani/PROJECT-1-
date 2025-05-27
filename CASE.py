#Function for uppercase
def is_uppercase(char):
    return char.isupper()

#Function for lowercase
def is_lowercase(char):
    return char.islower()

#Main function
def main():
    #Input a character
    Char = input("Input character: ")

    #Checking for a single character
    if len(Char) == 1:
        if is_uppercase(Char):
            print("Character is Uppercase")
        elif is_lowercase(Char):
            print("Character is Lowercase")
        else:
            print("Please enter a letter")
    else:
        print("Invalid entry")
        
main()

