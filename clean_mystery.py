import random

print("""Welcome to Mystery Word!""")

def get_random_word(word):
    """Opens a file, chooses a random word, and returns it"""
    word = random.choice(open('words.txt').read().split()).strip().casefold()

    return word

def display_word(word, blanks, guess):
    """Generates the word, including correct guesses and blanks"""
    result = ""
  
    for i in range(len(word)):
        if word[i] == guess:
            result = result + guess 
        else:
            result = result + blanks[i]   
    return result

def play_game(word):
    """ Runs Game Loop, calling other functions for nec. tasks """
    word = get_random_word('')
    blanks = "_" * len(word)
    guesses_left = 8
    guesses = []
    print(word) ###! Printing for now so I can see it

    while guesses_left > 0 and not blanks == word:
        print(blanks)
        print (f"You have {guesses_left} guesses left.")
        print (f"So far you've guessed {guesses}")
 
        guess = input("Guess a letter: ").casefold()

        if len(guess) != 1:
            print ("try again")    
        elif guess in word:
            print (f"'{guess}' is in the word!")
            blanks = display_word(word, blanks, guess)
        else:
            print (f"'{guess}' is not in the word!")
            guesses.append(guess)
            guesses_left -= 1

    if guesses_left <= 0:
        print ("You loose. The word was: " + str(word))
    else:
        print("You win! The word was: " + str(word))

play_game('word')