# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    complete_flag = 1
    for letter in secret_word:
        if letter not in letters_guessed:
            complete_flag = 0
    
    if complete_flag == 0:
        return False
    else:
        return True        


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guess += letter
        else:
            guess += "_ "
    return guess




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase

    available_letters = ""
    
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter
    
    return available_letters       
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string

    num_guesses = 6
    num_warnings = 3
    letters_guessed = []
    vowels = ['a','e','i','o','u']

    unique_letters_in_secretword = []
    for s in secret_word:
        if s not in unique_letters_in_secretword:
            unique_letters_in_secretword.append(s)

    num_unique_letters = len(unique_letters_in_secretword)        

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secret_word))+ " letters long.")
    print("-----------")
    print("You have "+ str(num_warnings)+ " warnings left.")
    print("You have "+ str(num_guesses)+ " guesses left.")
    print("Available letters:" + string.ascii_lowercase)

    while num_guesses > 0:
        guess = input("Please guess a letter:")
        

        if not str.isalpha(guess) and num_warnings > 0:
       		num_warnings -= 1
        	print("Oops! That is not a valid letter. You have "+str(num_warnings)+" warnings left: "+get_guessed_word(secret_word,letters_guessed))
        elif guess in letters_guessed and num_warnings > 0:
        	num_warnings -= 1
        	print("You already guessed that letter. You have "+str(num_warnings)+" warnings left: "+get_guessed_word(secret_word,letters_guessed))
        elif not str.isalpha(guess) and num_warnings == 0:
       		num_guesses -= 1
        	print("Oops! That is not a valid letter. You've been warned. You lose a guess: "+get_guessed_word(secret_word,letters_guessed)) 	
        elif guess in letters_guessed and num_warnings == 0:
        	num_guesses -= 1
        	print("You already guessed that letter. You've been warned. You lose a guess: "+get_guessed_word(secret_word,letters_guessed))
        else:
        	if not str.islower(guess):
        		guess = str.lower(guess)
        	letters_guessed.append(guess)



	        if guess in secret_word:
	            print("Good guess: "+get_guessed_word(secret_word,letters_guessed))
	        else:
	            print("Oops! That letter is not in my word: "+get_guessed_word(secret_word,letters_guessed))
	            if guess in vowels:
	            	num_guesses -= 2
	            else:
	            	num_guesses -= 1 

        if is_word_guessed(secret_word,letters_guessed):
            total_score = num_unique_letters*num_guesses
            print("Congrats! You Won. Your score is "+str(total_score))
            num_guesses = 0
        elif num_guesses <= 0:
            print("Out of Guesses. You Lose. The word was: "+secret_word)
        else:    		        	       
        	print("-----------")    
        	print("You have "+ str(num_guesses)+ " guesses left.")
        	print("Available letters:" + get_available_letters(letters_guessed) )  


    return

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_space_rmvd = my_word.replace(" ","")
    

    unique_letters_in_word = []
    for s in my_word_space_rmvd:
        if s not in unique_letters_in_word and s != "_":
            unique_letters_in_word.append(s)


    if len(my_word_space_rmvd) != len(other_word):
        return False
    else:
        match = 1
        for s in range(len(my_word_space_rmvd)):
            if my_word_space_rmvd[s] != "_" and my_word_space_rmvd[s] != other_word[s]:
                match = 0

        if match == 1:
            for s in unique_letters_in_word:
                count_my_word = 0
                count_other_word = 0
                for t in range(len(my_word_space_rmvd)):
                    if my_word_space_rmvd[t] == s:
                        count_my_word += 1
                    if other_word[t] == s:
                        count_other_word += 1
                if count_my_word != count_other_word:
                    match = 0            




        if match == 1:
            return True
        else:
            return False    



    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    match_list = []

    for s in wordlist:
        if match_with_gaps(my_word,s):
            match_list.append(s)


    if match_list == []:
        print("No matches found")
    else:
        proper_list = ""
        for i in match_list:
            proper_list = proper_list+" "+i
        print(proper_list)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string

    num_guesses = 6
    num_warnings = 3
    letters_guessed = []
    vowels = ['a','e','i','o','u']

    unique_letters_in_secretword = []
    for s in secret_word:
        if s not in unique_letters_in_secretword:
            unique_letters_in_secretword.append(s)

    num_unique_letters = len(unique_letters_in_secretword)        

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secret_word))+ " letters long.")
    print("-----------")
    print("You have "+ str(num_warnings)+ " warnings left.")
    print("You have "+ str(num_guesses)+ " guesses left.")
    print("Available letters:" + string.ascii_lowercase)

    while num_guesses > 0:
        guess = input("Please guess a letter:")
        
        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))

        else:    

            if not str.isalpha(guess) and num_warnings > 0:
                num_warnings -= 1
                print("Oops! That is not a valid letter. You have "+str(num_warnings)+" warnings left: "+get_guessed_word(secret_word,letters_guessed))
            elif guess in letters_guessed and num_warnings > 0:
                num_warnings -= 1
                print("You already guessed that letter. You have "+str(num_warnings)+" warnings left: "+get_guessed_word(secret_word,letters_guessed))
            elif not str.isalpha(guess) and num_warnings == 0:
                num_guesses -= 1
                print("Oops! That is not a valid letter. You've been warned. You lose a guess: "+get_guessed_word(secret_word,letters_guessed))     
            elif guess in letters_guessed and num_warnings == 0:
                num_guesses -= 1
                print("You already guessed that letter. You've been warned. You lose a guess: "+get_guessed_word(secret_word,letters_guessed))
            else:
                if not str.islower(guess):
                    guess = str.lower(guess)
                letters_guessed.append(guess)



                if guess in secret_word:
                    print("Good guess: "+get_guessed_word(secret_word,letters_guessed))
                else:
                    print("Oops! That letter is not in my word: "+get_guessed_word(secret_word,letters_guessed))
                    if guess in vowels:
                        num_guesses -= 2
                    else:
                        num_guesses -= 1 

            if is_word_guessed(secret_word,letters_guessed):
                total_score = num_unique_letters*num_guesses
                max_score = num_unique_letters*6
                print("Congrats! You Won. Your score is "+str(total_score)+" out of a potential "+str(max_score))
                num_guesses = 0
            elif num_guesses <= 0:
                print("Out of Guesses. You Lose. The word was: "+secret_word)
            else:                              
                print("-----------")    
                print("You have "+ str(num_guesses)+ " guesses left.")
                print("Available letters:" + get_available_letters(letters_guessed) )  


    return


 
  
  

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#secret_word = "d_ o_ ugg"
#hangman(secret_word)

 
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
