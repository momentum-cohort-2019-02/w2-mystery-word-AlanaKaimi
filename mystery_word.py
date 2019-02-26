
###* WORKS: Generate a Random word from a file 
###* WORKS: Asks user for a guess & difficulty
###* WORKS: Display '_' and correct user guesses
###* WORKS: Let's user know if guess is wrong or
    #*      right
###* WORKS: Get game to store and print out   
    #*      letters guessed
###* WORKS: Displays num of guesses left
###* WORKS: Deprecates num of guesses when user  
    #*      guesses incorrectly
###* WORKS: Make sure game doesn't break over
    #*      letter casing
###* WORKS: Confirms Win or Loose

###! TODO: 

###TODO: Get game to generate the word based off difficulty


# Imports the random library, giving access to it's modules and allowing us the .random features
import random

###* WORKS --->
def get_user_difficulty(difficulty):
    difficulty = None
    while difficulty not in ['easy', 'normal', 'hard']:
        difficulty = input("Choose your level: [easy, normal, hard]: ")
    print(f"You chose {difficulty}. Let's get started!")
###* <--- WORKS

###! TODO: Get game to generate the word based off difficulty

###!  Testing --->

def filter_word_list_by_difficulty(word_list, difficulty):
    """
    Given a list of words and difficulty level
    filter that list
    """
    filtered_word_list = []
    for word in word_list:
        if difficulty == 'easy' and 4 <= len(word) <= 6:
            filtered_word_list.append(word)
        elif difficulty == 'normal' and 6 <= len(word) <= 8:
            filtered_word_list.append(word)
        elif difficulty == 'hard' and len(word) >= 8:
            filtered_word_list.append(word)
        
        return filtered_word_list

###! <--- Testing ^

###* WORKS --->
# open file and get a list 
def get_word_list(filename):
    """
    Opens a file, chooses a random word, and returns it
    """
    with open(filename) as file:
        word_list =[line.strip().lower() for line in file]
    ### returns the chosen word
    return word_list
###* <--- WORKS

###* WORKS --->
def display_word(word, blanks, guess):
    """
    Generates the word, including correct guesses and blanks
    """
    result = ""
  
  # Adds guess to string if guess is correctly
    for i in range(len(word)):
        if word[i] == guess:
            result = result + guess
    # Add the blank at index i to result if it doesn't match the guess  
        else:
            result = result + blanks[i]
  # Returns the result    
    return result
###* <--- WORKS

###* WORKS --->
def play_game(word):
    """
    Runs Game Loop, calling other functions for nec. tasks
    """
    # welcomes user to game
    print("Welcome to Mystery Word!")
    difficulty = get_user_difficulty('')
    word_list = get_word_list('words.txt')
    word_list = filter_word_list_by_difficulty(word_list, difficulty)
    word = random.choice('word_list')
    blanks = "_" * len(word)
    guesses_left = 8
    guesses = []
    print(word) ###! REMOVE: Printing for now so I can see it

###* Game loop --->
    while guesses_left > 0 and not blanks == word:
        print(blanks)
        print (f"You have {guesses_left} guesses left.")
        print (f"So far you've guessed {guesses}")
    # get's user's guess 
        guess = input("Guess a letter: ").casefold()
    # response if guess is invalid
        if len(guess) != 1:
            print ("try again")
    
    # response if guess is correct
        elif guess in word:
            print (f"'{guess}' is in the word!")
    # updates the display word
            blanks = display_word(word, blanks, guess)
    # response if guess is wrong
        else:
            print (f"'{guess}' is not in the word!")
    # stores and prints out incorrect guesses
            guesses.append(guess)
    # updates the # of guesses left
            guesses_left == 0

### Still declares win... very affirmative robot <3 *fixed 
# response if all gueses are used
    if guesses_left <= 0:
        print ("You loose. The word was: " + str(word))
# response if we win!
    else:
        print("You win! The word was: " + str(word))
###* <--- WORKS

###* WORKS --->
# Only runs function when running this file, not on import
if __name__ == "__main__":
# Calls the function that sets the game into play!
    play_game('word')
###* <--- WORKS