# Problem Set 2, hangman.py
# Name: sommio
# Collaborators:
# Time spent: ~2d

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            secret_word = secret_word[0:i] + '*' + secret_word[i+1:]
    return secret_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
    return available_letters


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    used_letters = [] # letters used by the user
    letters_guessed = []  # letters successfully guessed by user

    def game_setup():
        """
        Prints the game start message and return None
        """
        print('Welcome to Hangman!')
        print(f'I am thinking of a word that is {len(secret_word)} letters long.')
        print('--------------')

    def is_legal_input(guess):
        """
        guess: string, user input
        Checks if user input is legal, return a boolean
        """
        if len(guess) != 1:
            return False
        elif with_help and guess == '!':
            return True
        elif guess not in string.ascii_lowercase:
            return False
        return True
    
    def is_correct_input(guess):
        """
        guess: string, user input
        Checks for correct user input, and operates on the lists `used_letters`
        and `letters_guessed`, return a boolean
        """
        used_letters.append(guess)
        if guess in secret_word:
            letters_guessed.append(guess)
            return True
        return False
    
    def is_available_letter(guess):
        """
        guess: string, user input
        Checks if user input is available, return a boolean value
        """
        if guess not in used_letters:
            return True
        return False
    
    def reveal_letter(word_progress):
        """
        word_progress: string, Return of get_word_progress function
        Reveals an unguessed letter by manipulating the lists 
        `used_letters` and `letters_guessed`, return the revealed letter
        """
        choose_from = ''
        for char in secret_word:
            if char not in word_progress.replace('*',''):
                choose_from += char
        new = random.randint(0, len(choose_from)-1)
        revealed_letter = choose_from[new]
        used_letters.append(revealed_letter)
        letters_guessed.append(revealed_letter)
        return revealed_letter

    def user_interaction():
        """
        Responsible for user interaction and `guesses_left` counting, ends and
        return `guesses_left` after a successful user guess or `guesses_left` is 0

        List operations are done by other helper functions
        """
        guesses_left = 10
        word_progress = ''
        guess_letter = '' # user input
        while guesses_left != 0 and word_progress != secret_word:
            word_progress = get_word_progress(secret_word, letters_guessed)
            available_letter = get_available_letters(used_letters)

            print(f'You have {guesses_left} guesses left.')
            print(f'Available letters: {available_letter}')

            guess_letter = input('Please guess a letter: ').lower()
            if not is_legal_input(guess_letter):
                print('Oops! That is not a valid letter. Please input a letter from')
                print(f'the alphabet: {word_progress}')
            elif with_help and guess_letter == '!':
                if guesses_left > 3:
                    revealed_letter = reveal_letter(word_progress)
                    # Refresh word_progress after reveal
                    word_progress = get_word_progress(secret_word, letters_guessed)
                    guesses_left -= 3
                    print(f'Letter revealed: {revealed_letter}')
                    print(word_progress)
                else:
                    print(f'Oops! Not enough guesses left: {word_progress}')
            elif not is_available_letter(guess_letter):
                print(f'Oops! You\'ve already guessed that letter: {word_progress}')
            elif is_correct_input(guess_letter):
                # Refresh word_progress after a correct guess
                word_progress = get_word_progress(secret_word, letters_guessed)
                print(f'Good guess: {word_progress}')
            else:
                if guess_letter in 'aeiou':
                    guesses_left -= 2
                else:
                    guesses_left -= 1
                print(f'Oops! That letter is not in my word: {word_progress}')
            print('--------------')
        return guesses_left
    
    def total_score(guesses_left):
        '''
        guesses_left: int, Returned by the `user_interaction()` function
        '''
        word_length = len(secret_word)
        unique_letter = ''
        for char in secret_word:
            if char not in unique_letter:
                unique_letter += char
        return (guesses_left + 4*len(unique_letter)) + (3*word_length)
    
    def game_termination(guesses_left):
        '''
        guesses_left: int, Returned by the `user_interaction()` function
        '''
        if guesses_left != 0:
            score = total_score(guesses_left)
            print('Congratulations, you won!')
            print(f'Your total score for this game is: {score}')
        else:
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

    game_setup()
    game_termination(user_interaction())


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test
if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    # secret_word = "wildcard"
    # with_help = True
    # hangman(secret_word, with_help)
