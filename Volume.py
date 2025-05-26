#Import library
import math 
print("The value pi is:", math.pi)

#Input the radius
radius = input("Input radius: ")
if radius.isdigit():
    r = float(radius)

    #Calculating volume of a sphere
    Volume = (4/3) * math.pi * (r**3) #r**3 exponential operator

    print(f"Volume = {Volume} cubic units")
else:
    print("Invalid entry")
