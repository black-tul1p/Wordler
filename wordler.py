#! /usr/bin/python3

# Author: github.com/black-tul1p

#############################  IMPORTS  ################################
import enum, random, collections

#############################  CLASSES  ################################

class Letter_Type(enum.Enum):
	INCORRECT = 0
	PRESENT 	= 1
	CORRECT 	= 2

############################ GLOBAL VARS  ##############################
wordfile  = "wordle_words.txt"
best_word = "RAISE"
wordlist  = []

title = '''
┌───────────────────────────────────────────────────────────────────────┐
│                           Welcome to Wordler!                         │
└───────────────────────────────────────────────────────────────────────┘
'''

help_text = '''\n
┌───────────────────────────────────────────────────────────────────────┐
│                                  HELP                                 │
├───────────────────────────────────────────────────────────────────────┤
│ You can either enter a custom word and its score or just the score    │
│ for the suggested word .                                              │
│                                                                       │
│ Format for the score: #####                                           │
│ > Example: 00201                                                      │
│                                                                       │
│ Possible values for #:                                                │
│   > 0 : Incorrect                                                     │
│   > 1 : Wrong Position                                                │
│   > 2 : Correct                                                       │
├───────────────────────────────────────────────────────────────────────┤
│ P.S. it's ok if you use this program for solves, no one will know :)  │
│                                                                       │
│                                                          ~ black-tul1p│
└───────────────────────────────────────────────────────────────────────┘
'''

end_text = '''
┌───────────────────────────────────────────────────────────────────────┐
│                      Thank you for using Wordler!                     │
└───────────────────────────────────────────────────────────────────────┘
'''

########################################################################


##############################  FUNCTION  ##############################
# - Inputs  : User guess and word to check against					   #
# - Outputs : Array of score values for each char in the guess string  #																									   #
# - Desc	: A function that calculates accuracy score of a guess	   #
########################################################################
def get_score(word, guess):
	score = []
	maybe = collections.Counter(w for w, g in zip(word, guess) if w != g)

	# Calculate score for guess against word
	for guess_char, word_char in zip(guess, word):
		if guess_char == word_char:
			score.append(Letter_Type.CORRECT)
		elif guess_char in word_char and maybe[guess_char] > 0:
			score.append(Letter_Type.PRESENT)
			maybe[guess_char] -= 1
		else:
			score.append(Letter_Type.INCORRECT)

	return score


##############################  FUNCTION  ##############################
# - Inputs  : List of possible words								   #
# - Outputs : Final list of words									   #
# - Desc	: A function that takes user input for guesses in a loop   #
########################################################################
def play(wordlist):
	counter = 0
	mapping = {"0": Letter_Type.INCORRECT, "1": Letter_Type.PRESENT, "2": Letter_Type.CORRECT}
	while len(wordlist) > 1:
		# Get random word from list of possible words
		if counter == 0:
			guess = best_word
			print(f"│ Start by giving {guess!r} a try...\n")
		elif counter == 1:
			guess = get_opp_word(best_word)
			print(f"│ Now, give {guess!r} a go...\n")
		else:
			guess = get_word(wordlist)
		
		# Get custom guess from user if needed
		c_input = input("Enter a custom guess or score for suggested word (or \"h\" for help): ")
		c_input = c_input.strip().upper()
		score = ""

		# Input verification loop
		while (not c_input.isalpha() and not c_input.isnumeric()) and (len(c_input) != 5 or c_input.lower() != "h"):
			c_input = input("│ Incorrect input, please try again: ")
		if c_input.isnumeric():
			score = c_input.strip()
		elif c_input.lower() == "h":
			print(help_text)
			counter -= 1
		else:
			guess = c_input
			while not score.isnumeric() or len(score) != 5:
				score = input("Enter the score: ")

		# Case when guess is completely right
		if score == "22222":
			print("\n│ You did it!")
			return "WIN"

		# Create score array and update list of possible words
		score_array = [mapping[char] for char in score if char in mapping]
		wordlist = update_list(wordlist, guess, score_array)
		print()
		counter += 1
	
	return wordlist.pop()


##############################  FUNCTION  ##############################
# - Inputs  : Complete list of possible words						   #
# - Outputs : Random second best guess string						   #
# - Desc	: A function that returns a random guess containing no	   #
#			  letters from the best guess		  					   #
########################################################################

def get_opp_word(guess):
	possible_words = []
	og_wlist = []
	with open(wordfile, "r") as file:
		og_wlist = [word.strip().upper() for word in file.readlines()]

	for word in og_wlist:
		flag = 0
		# Set flag if word contains characters from original guess
		for word_char in word:
			if word_char in guess:
				flag = 1
				break
		# Make sure characters are not present in original guess
		# and make sure all letters are unique
		if flag != 1 and len(set(word)) == len(word):
			possible_words.append(word)

	return random.choice(possible_words)


##############################  FUNCTION  ##############################
# - Inputs  : List of possible words								   #
# - Outputs : Random guess string									   #
# - Desc	: A function that returns a random guess from wordlist	   #
########################################################################
def get_word(wordlist):
	print(f"│ I see {len(wordlist)} possibilities...")
	guess = random.choice(wordlist)
	print(f"│ Try guessing {guess!r}...\n")
	return guess


##############################  FUNCTION  ##############################
# - Inputs  : Current list of words, guess string, score array		   #
# - Outputs : Array containing possible guesses   					   #
# - Desc	: A function updates list of possible words based		   #
########################################################################
def update_list(words, guess, score):
	possible_words = []

	for word in words:
		maybe = collections.Counter(w for w, s in zip(word, score) if s != Letter_Type.CORRECT)
		# Add word to updated list if it passes all the cases below
		for word_char, guess_char, value in zip(word, guess, score):
			# CASE: Missing correct character
			if word_char != guess_char and value == Letter_Type.CORRECT:
				break
			# CASE: Incorrect Guess
			elif word_char == guess_char and value != Letter_Type.CORRECT:
				break
			# CASE: Missing present character 
			elif value == Letter_Type.PRESENT:
				if not maybe[guess_char]:
					break
				maybe[guess_char] -= 1
			# CASE: Contains absent character
			elif value == Letter_Type.INCORRECT and maybe[guess_char]:
				break
		else:
			possible_words.append(word)

	return possible_words


############################ MAIN FUNCTION  ############################

if __name__ == '__main__':
	with open(wordfile, "r") as file:
		wordlist = [word.strip().upper() for word in file.readlines()]

	print(title)
	word = play(wordlist)

	if not word:
		print(f"│ Sorry, the word isn't present in my wordlist :/")
	elif word != "WIN":
		print(f"│ The word is {word!r}!")

	print(end_text)

########################################################################
