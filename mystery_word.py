# Imports the random library, giving access to it's modules and allowing us the .random features
import random
# welcomes user to game
print("""Welcome to Mystery Word!""")

###* WORKS --->
# open file and choose a random word 
def get_random_word(word):
    """Opens a file, chooses a random word, and returns it"""
    word = random.choice(open('words.txt').read().split()).strip()

     ### returns the chosen word
    return word
###* <--- WORKS

###* WORKS --->
def display_word(word, cur_blank, user_guess):
    """Generates the word, including correct guesses and blanks"""
    result = ""
  
  # Adds guess to string if guess is correctly
    for i in range(len(word)):
        if word[i] == user_guess:
            result = result + user_guess     

    # Add the blank at index i to result if it doesn't match the guess  
        else:
            result = result + cur_blank[i]
  ### Returns the result    
    return result
###* <--- WORKS

###* WORKS --->
def play_game(word):
    word = get_random_word('')
    blanks = "_" * len(word)
    guesses_left = 8
    print(word) ### Printing for now so I can see it

### Game loop


    while guesses_left > 0 and not blanks == word:
        print(blanks)
        print (str(guesses_left))
    # get's user's guess
        guess = input("Guess a letter: ")
    # response if guess is invalid
        if len(guess) != 1:
            print ("try again")
    # response if guess is correct
        elif guess in word:
            print ("It's in the word!")
    # updates the display word
            blanks = display_word(word, blanks, guess)
    # response if guess is wrong
        else:
            print ("not in the word!")
    # updates the # of guesses left
            guesses_left -= 1

### Still declares win... very affirmative robot <3 *fixed 
# response if all gueses are used
    if guesses_left < 1:
        print ("You loose. the word was: " + str(word))
# response if we win!
    else:
        print("You win!")
###* <--- WORKS


###TODO 

### Asks user for difficulty but it doesn't really connect it to the game :/
    # difficulty = input("Choose difficulty (easy, medium, hard): ")

### Get game to generate the word based off difficulty

### Get game to print out letters guessed



###* WORKS --->
play_game('word')
###* <--- WORKS