#Letter counter app
print("\n Welcome to Bosco's letter counter app\n")
name = input("What's your name").capitalize()
print(f"\nHello {name}")

sentence  = input("Enter sentence: ")
word = input("Enter word you want to count")
print(f"this is how many {word}'s are in your sentence ={sentence.count(word)}")