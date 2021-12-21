#the right triangle solver app
import math
print("\nWelcome to the hipotinuse solver app\n")
side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
total = side1**2 + side2**2
hipotenuse = math.sqrt(total)
print(f"The hipotenuse is = {hipotenuse}")