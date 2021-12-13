def get_info():
  print("\n\t\t Welcome to Aussiebank!\n")
  global name
  name = input("what's your name?: ")
  global deposit1
  global deposit2
  deposit1 = int(input(f"\n\n Hello {name}\n\nPlease enter how much money you want towards your savings account: "))
  deposit2 = int(input(f"\n Now enter how much money you want towards your checking account: "))
  global dict1
  dict1 = {"name":name,"savings account":deposit1,"checking account":deposit2}
  print(f"\n\n This is your current account information ==> \t\t{dict1}\n\n")  
  return dict1

get_info()


def transaction():

    type_account = input("Do you want to access your savings account or checking account---> ")
    bank_account = dict1
    while "savings" in type_account:
        print("\nYou have selected your savings account\n")
        input2= input("Enter if you wish to make a deposit or withdrawal---> ")
        if "deposit" in input2:
            print(f"\nYou have selected to deposit into {name}'s' account\n ")
            input3 = int(input("How much money do you want to deposit: "))
            bank_account["savings account"] = deposit1 + input3
            print(f"\nYou have added {input3}€ into your savings account\n")
            print(f"\n\n This is your new account information ==> \t\t{bank_account}\n\n")
            break
        elif "withdrawal"in input2:
            print("\n\nYou have selected to withdrawal\n\n")
            input4 = int(input("Enter how much would you like to withdrawal from your savings account: "))
            bank_account["savings account"] = deposit1 - input4
            print(f"\nYou have taken {input4}€ of your savings account\n")
            print(f"\n\n This is your new account information ==> \t\t{bank_account}\n\n")
            break
    while "checking" in type_account:
        print("\nYou have selected your checking account\n")
        input5= input("Enter if you wish to make a deposit or withdrawal---> ")
        if "deposit" in input5:
            print(f"\n You have selected to deposit into {name}'s' account \n ")
            input6 = int(input("How much money do you want to deposit: "))
            bank_account["checking account"] = deposit2 + input6
            print(f"\nYou have added {input6}€ into your checking's account\n")
            print(f"\n\n This is your new account information ==> \t\t{bank_account}\n\n")
            break
        elif "withdrawal"in input5:
            print("\n\nYou have selected to withdrawal\n\n")
            input7 = int(input("Enter how much would you like to withdrawal from your checking account: "))
            bank_account["checking account"] = deposit2 - input7
            print(f"\nYou have taken {input7}€ of your checking account\n")
            print(f"\n\n This is your new account information ==> \t\t{bank_account}\n\n")
            break
        else:
            print("\n\nThe mode you have selected does not exist\n\n") 
            type_account =  input("Do you want to access your savings account or checking account---> ")
   


transaction()


def continued():
  input8 = input("Do you want to continue?:Y/N=>")
  if "Y" in input8:
    print(transaction())
  elif "N" in input8:
    print(f"\n\nGoodbye {name},\n\nHave a good Day!")


continued()