import random
###TODO Most of it! Sorry for the mess!

# print("""Welcome to Mystery Word!
#     Choose your level of difficulty:
#     Easy: 4-6 characters
#     Normal: 6-8 characters
#     Hard: 8+ characters""")
# ### * WORKS!

# Let user choose dificulty level of easy: 4-6 char normal: 6-8 char, and Hard 8+ char
    #  Read words from a file words.txt
    # choose only words of a certain length
        # filter a list by string size
    # get random entry from list
        #random module? 
# ### * WORKS!
# diff_choice = input("Difficulty level: ")
# ### * WORKS!

# ### * WORKS!
# def choose_difficulty(diff_choice): 
# # .casefold() allows user to input answer in any case and it will be accepted     
#     diff_choice = diff_choice.casefold()
# # responds to user's choice input
#     if diff_choice == ("easy"):
#         print(f"{diff_choice} 4-6 letters")
#     elif diff_choice == ("normal"): 
#         print(diff_choice + " 6-8 letters")
#     elif diff_choice == ("hard"):
#         print(diff_choice + " 8+ letters")
   
# ### * WORKS!

# choose_difficulty(diff_choice)


###* WORKS 
# open file and choose a random word 
def get_random_word(word):
    word = random.choice(open('words.txt').read().split()).strip()
    return word

print(get_random_word('word'))
###* WORKS

###TODO
def display_word(secret_word):
    secret_word = get_random_word('word')
    dashes = "_" * len(secret_word)
    guesses_left = 8
    

    # while guesses_left > -1 and not dashes == secret_word:
    print (len(secret_word))
    print(dashes)
    print (str(guesses_left))
print(display_word('secret_word'))



# --based off of difficulty level (# of characters)



# def choose_word(filename):
#     """Read in `file` and choose word based on difficulty level"""
    
#     with open("words.txt") as file:
#         text = file.read

#         text = normalize_text(text)
#         words = []

#     for word in text.split(" "):
#         words.append(word)

#     for word in sorted(words, key=words.get):
#         easy_words = 
#         medium_words =
#         hard_words =

# Find the length of word

# def word_length(word_list):
#     """Given a list, go through and find the length of a word"""
#     word_count = {}
#     for word in list_list:
#         if word not in word_count:
#         word_count[word] = 1

#         else:
#             word_count[word] += 1
        
#         return word_count
        
# call function
### * WORKS!
# choose_difficulty (diff_choice)
### * WORKS!
# choose_word (filename)



    

# Print how many chars the word contains

# get 1 letter from user per round
    # casefold it
    # check that it's one letter
    # if more than 1 print invalid

# Display partially guessed words








# print a word guesses like B_ _ BA_D



