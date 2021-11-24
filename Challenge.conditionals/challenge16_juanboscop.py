#shipping cost app
def shipping():
    print("\nWelcome to bosco's shopping fee app ====> ")
    print("""
        \nFrom 0 to 100 orders costs   = $5.10/ud
        \nFrom 100 to 500 orders cost  = $5.00/ud
        \nFrom 500 to 1000 orders cost = $4.95/ud
        \nFor shipping over 1000 cost  = $4.80/ud
                                               """)
    items = int(input("\n\t\t\t------> How many units do you request?:"))
    if items in range(1,100):
       total1 = round(float(items * 5.10 ),2)
       print(f"\nThe {items} units you requested cost ${total1}\n")
    elif items in range(100,500):
        total2 = round(float(items * 5.00),2)
        print(f"\nThe {items} units you requested cost ${total2}\n")
    elif items in range(500,1000):
        total3 = round(float(items * 4.95),2)
        print(f"\nThe {items} units you requested cost ${total3}\n")
    else:
        total4 = round(float(items * 4.80),2)
        print(f"\nThe {items} units you requested cost ${total4}\n")
    cont = input("\n\t\t\t----> Do you wish to finalize this decision? y/n").lower()
    if "y" in cont:
        print("\nHave a Great day!\n Thanks for trusting bosco's shopping app.\n")
    elif "n"in cont:
        print("\nI'm sorry\n How much units did you really want?:\n")
        shipping()

 
    






while True:
  userlist = ['bosco','immune','ceb','alumno']
  passw = input("\nEnter your username:\n").lower()
  if passw in userlist:
      shipping()
      break
  elif passw not in userlist:
      print("\nI'm sorry\nBut we don't recognize your username\nplease try starting the program again....")

