def substract(num1,num2):
    total = round(float(num1 - num2),4)
    print(f"\nThe substraction of {num1} - {num2} = {total}")

def multiply(num1,num2):
    total = round(float(num1 * num2),4)
    print(f"\nThe multiplication of {num1} x {num2} = {total}")

def divide(num1,num2):
    total = round(float(num1/num2),4)
    if num1 or num2 == 0:
        print("\nDIVISON ERROR\n\n==> you cant divide with 0")
    else:
        print(f"\nThe division of {num1} divided by {num2} = {total}")

def exponent(num1,num2):
    total = round(float(num1**num2),4)
    print(f"\nThe exponent of {num1} to the power of {num2} = {total}")

def add(num1,num2):
    total = round(float(num1 + num2),4)
    print(f"\nThe sum of {num1} + {num2} = {total}")

while True:
    print("\n\t\t--> Welcome to bosco's calculator app <--\n")
    num1 = float(input("Enter number 1 = "))
    num2 = float(input("\nEnter number 2 = "))
    mode = input("\nEnter add,substract,divide,exponent or multiply --> ").lower()
    if mode == "add":
        add(num1,num2)
    elif mode == "substract":
        substract(num1,num2)
    elif mode == "multiply":
        multiply(num1,num2)
    elif mode == "exponent":
        exponent(num1,num2)
    elif mode == "divide":
        divide(num1,num2)
    else:
        print("\nThe mode you have typed does not exist,please try again!\n")
        mode = input("\nEnter add,substract,divide,exponent or multiply --> ").lower()
    again = input("Would you like to run the program again? y/n").lower()
    if again == "n":
        print("\nGoodbye\n")
        break
    


    






