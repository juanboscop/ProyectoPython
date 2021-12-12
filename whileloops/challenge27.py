print("\n\t\t--> Welcome to bosco's Even odd number sorter app <--\t\t\n")
flag = True
while flag:
    num = input("\n\tEnter numbers separated by (,) = ")
    list1 = []
    list1 = num.split(",")
    num_list = list1
    even = []
    odd = []
    int_list = list(map(int, list1))
    for number in int_list:
        if number % 2 ==0:
            even.append(f"\n\t\t ==> The number {number} is even")
        if number % 2 > 0:
            odd.append(f"\n\t\t ==> The number {number} is odd")
    for item in even:
        print(item)
    for i in odd:
        print(i)
    cnt = input("\t\t\t\t---> Would you like to continue  Y/N: ").upper()
    if cnt == "N":
        flag = False
        

print("\n GoodBye,Have a great day.\n")



          

    
    
        


