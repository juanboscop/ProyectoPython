import random
print("\n\t\t--> Welcome to bosco's guess my word app <--\n")
game_dict = {"sports":["basketball","football","volleyball","rugby"],
             "body part":["arm","leg","hands","head"],
             "subjects":["english","math","science","physics"]
                                                                }
name = input("\n\t--> Hello what's your name: ")
game_keys = []
for key in game_dict:
    game_keys.append(key)

flag = True
while flag:
    game_category = random.choice(game_keys)
    game_word = random.choice(game_dict[f"{game_category}"])
    blank_word = []
    letters = len(game_word)
    for letters in game_word:
        blank_word.append("-")
    print(f"\nWelcome {name} you have to guess a word from the following category = {game_category}\n")
    slash = ""
    guess = ""
    guess_count = 0
    while True:
        print(slash.join(blank_word))
        guess = input("\n\t--> Enter guess: ").lower()
        guess_count += 1
        letter = "abcdefghijklmnopqrstuvwxyz"
        if guess == game_word:
            print("\nWell Done!,You have beaten the game\n")
            cont = input("\nWould you like to start program again Y/N").upper()
            if "Y" in cont:
                print("You have chosen to keep playing")
            else:
                print("\nGoodbye\n")
                break
        else:
            print("You guessed incorrectly")
            for guess_count in range(1+guess_count):
                guess.replace("-",random.choice(letter))
            print(guess)
 
        flag = False
        
        
        


    

    
    
    
