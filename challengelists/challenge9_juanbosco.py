print("welcome to the basketball roster program")
point =input("\nWho is your point guard ? ").title()
shooting =input("Who is your shooting guard? :").title()
small = input("who is your small forward?: ").title()
power = input("who is your power forward? :").title()
center = input("who is your center?: ").title()
print("\n")
print("This is your starting 5 for this season:")
print(f"""\n Point guard =             {point}
shooting guard =             {shooting}
small forward  =             {small}
power forward  =             {power}
      center   =             {center}""")
list1= [point,shooting,small,power,center]
list1.remove(center)
print("\n\n")
print(f"\n OH NO your player {small} has been injured you will have to replace him")
injured=input("\n Who would you like to replace him ")
print("\nYour new starting 5 for this season is: ")
print(f"""\n Point guard =             {point}
shooting guard =             {shooting}
small forward  =             {injured}
power forward  =             {power}
      center   =             {center}""")
print("")
print(f"Good luck {injured} You will do great!")


