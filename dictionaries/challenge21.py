print("\n\t\t---> Welcome to bosco's dictionary\n")

thesaurus = {"pretty":["beautiful","good-looking","radiant","exquisite"],
             "ugly":["monstrous","hideous","foul","repulsive"],
             "fast":["agile","quick","swift","electric"],
             "slow":["sluggish","gradual","passive","imperceptible"] }
while True:
    print("These are your registered synonyms===>\n\npretty.\nugly.\nfast.\nslow.")
    synonym = input("\nChoose one --> ").lower()
    if "pretty" in synonym:
        print("Some synonyms for pretty are = ",thesaurus["pretty"])
    elif "ugly" in synonym:
        print("Some synonyms for ugly are = ",thesaurus["ugly"])
    elif "fast" in synonym:
        print("Some synonyms for fast are = ",thesaurus["fast"])
    elif "slow" in synonym:
         print("Some synonyms for slow are = ",thesaurus["slow"])
    else:
        print("We currently don't have that word in our dictionary\n\n-----> Choose one mentioned above")
    choice = input("\n\n Do you want another synonym or quit\n\n\t\t--> Type synonym or quit\n").lower()
    if "synonym" in choice:
        print("\n Continued===>\n")
    elif "quit"in choice:
        print("\nGoodbye\nThank you for using bosco's dictionary")
        break

        
    
    
    





 
             

