#Voting app
print("\n\t\t\t\t\t-----> Welcome to Bosco's voting app ===>")
def voting():
    print("\n\t\tWelcome\n")
    choices = ["republican","Democratic","Independent","Libertarian","Green"]
    print("\t\t\t\t-----> This are your choices <------")
    for item in choices:
        print("\n",item)



while True:
  name = input("\n\t\t--> Enter name: ")
  age = int(input("\n\t\t--> Enter age: "))
  print(f"Hello {name}")
  if age in range(0,18):
      print("\nYou are not over the age of 18\nCome back when you are.\n")
  else:
      voting()
      break
