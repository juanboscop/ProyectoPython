print("\nWelcome to Bosco's factorial python program\n")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n =int(input("Enter factorial number: "))
print(f"\n\t\t\t---> the factorial of {n}! is = {factorial(n)}")


