import random

print("\n\t\t--> Welcome to bosco's dice app <--\n")
def dice_sides():
    global sides
    sides = int(input("\nEnter sides of your dice = "))
dice_sides()


def dice_number():
    global number
    number = int(input("\nEnter how many times you would like to roll your dice = "))
dice_number()


def roll_dice():
    print(f"\nYou have rolled {number} times a {sides} sided dice\n\nThe results are the following ===>\n\n  ")
    for times in range(1,6):
        
        print(times)
roll_dice()
while True:
    again = input("\nWould you like to roll again y/n --> ").lower()
    if "y" == again:
        print(dice_sides)
        print(dice_number)
        print(roll_dice)
    else:
        print("\nGoodbye\nThank you for using my app!\n")
        break

