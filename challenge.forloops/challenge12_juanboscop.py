#Quadratic formula 
import cmath
import math

print("\nWelcome to bosco's quadratic formula program\n")

def equation():
        a = int(input("Enter the value of a "))
        b = int(input("Enter the value of b "))
        c = int(input("Enter the value of c "))
        d = (b**2) - (4*a*c)


        sol1 = (-b-cmath.sqrt(d))/(2*a)
        sol2 = (-b+cmath.sqrt(d))/(2*a)

        print('The solution are {0} and {1}'.format(sol1,sol2))


n_equation = int(input("how many equations do you want to do today:"))
number = 0
for number in range(n_equation):
    print("\nEnter equation: \n")
    equation()
    
    

    
