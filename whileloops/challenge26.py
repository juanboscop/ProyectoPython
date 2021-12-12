print("\n\t\t--> Welcome to bosco's factor generator app <--\t\t\n")
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = int(input("Enter the factor of the number = "))

print_factors(num)
while True:
    run_again = input("would you like to run the program again Y/N ==> ").upper()

    if run_again == "Y":
        num = int(input("Enter the factor of the number = "))
        print_factors(num)

    else:
        print("\ngoodbye user\n\nHave a good day.")
        break