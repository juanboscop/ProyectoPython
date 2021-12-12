print("\n\t\t--> Welcome to bosco's Prime number app <--\t\t\n")
flag = True
while flag:
    print("""
        \nPress 1 to choose a specific number and see if it's a prime number\n
        \nPress 2 to determine prime numbers within a determined range\n
                                                                         """)

    mode = input("\n\t--> Choose option 1 or 2: ")
    if "1" in mode:
        num = int(input("Enter number: "))
        for i in range(2, num):
            if (num % i) == 0:
                print(num,"is a prime number")
            else:
                