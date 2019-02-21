print("""Welcome to Mystery Word!
    Choose your level of difficulty:
    Easy: 4-6 characters
    Normal: 6-8 characters
    Hard: 8+ characters""")
# * works!



# Let user choose dificulty level of easy: 4-6 char normal: 6-8 char, and Hard 8+ char
    #  Read words from a file words.txt
    # choose only words of a certain length
        # filter a list by string size
    # get random entry from list
        #random module? 
diff_choice = input("Difficulty level: ")

def choose_difficulty(diff_choice): 
    
    diff_choice = diff_choice.casefold()
    if diff_choice == ("Easy"):
        print(diff_choice + " 4-6 letters")
    elif diff_choice == ("Normal"): 
        print(diff_choice + " 6-8 letters")
    elif diff_choice == ("Hard"):
        print(diff_choice + " 8+ letters")
        
# * works!

choose_difficulty (diff_choice)
# * works!

# Print how many chars the word contains

# get 1 letter from user per round
    # casefold it
    # check that it's one letter
    # if more than 1 print invalid

# Display partially guessed words








# print a word guesses like B_ _ BA_D



