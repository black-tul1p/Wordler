#! /usr/bin/python3

# Author: black-tul1p

##############################  TODO  ##################################
# 1. Add char list updates											   #
# 2. Add regex creator												   #
# 3. Add word getter												   #
# 4. Add guess displayer											   #
# 5. [OPTIONAL] Add a menu											   #
########################################################################

#############################  IMPORTS  ################################
import enum

#############################  CLASSES  ################################

class Let_Type(enum.Enum):
	INCORRECT = 0
	PRESENT = 1
	CORRECT = 2

############################ GLOBAL VARS  ##############################
wordfile  = "wordle-words.txt"
wordlist  = []
guesses   = []
probs     = []
letters   = []
guess_num = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']

help_text = '''
Format for entering guess:
  -> _#_#_#_#_#

  where:
    -> # is a probability value
    -> _ is a letter

  -> Example: W1O0R0D2S1

Probability values for #:
  -> 0 : incorrect
  -> 1 : wrong position
  -> 2 : correct
'''
########################################################################


##############################  FUNCTION  ##############################
# - Inputs  : User guess and word to check against										 #
# - Outputs : A score array of score values for each guess char 	 		 #																									   #
# - Desc		: A function that calculates accuracy score of a guess		 #
########################################################################
def get_score(word, guess):
	score = []
	maybe = collections.Counter(w for w, g in zip(word, guess) if w != g)

	for guess_char, word_char in zip(guess, word):
		if guess_char == word_char:
			score.append(Let_Type.CORRECT)
		elif guess_char in word_char and maybe[guess_char] > 0:
			score.append(Let_Type.PRESENT)
			maybe[guess_char] -= 1
		else:
			score.append(Let_Type.INCORRECT)

	return score


##############################  FUNCTION  ##############################
# - Inputs  : None																									   #
# - Outputs : None																									   #
# - Desc		: A function that takes user input for guesses in a loop 	 #
########################################################################
def guess_loop():
	for _ in range(6):
		# Get and store guess in array
		guess = ""
		while len(guess) != 10:
			guess = input("Enter the "+ guess_num[_]+ " guess: ")
			if (len(guess) != 10):
				print("[X] Please enter the guess in the correct format\n")
		guess = guess.lower().strip()
		guesses.append(guess)

		# Extract information from current guess
		curr_probs, curr_chars = extract_info(guess)

		print()
		#print(guesses)

##############################  FUNCTION  ##############################
# - Inputs  : The user-entered guess string													   #
# - Outputs : Arrays containing letters and probability from guesses   #
# - Desc		: A function that extracts information from guesses				 #
########################################################################
def extract_info(guess):
	curr_lett = []
	curr_prob = []
	for i in range(len(guess)):
		if (i+1) % 2 != 0:
			curr_lett.append(guess[i])
		else:
			curr_prob.append(int(guess[i]))	
	letters.append(curr_lett)
	probs.append(curr_prob)
	return curr_prob, curr_lett

##############################  FUNCTION  ##############################
# - Inputs  : The user-entered guess string													   #
# - Outputs : Arrays containing letters and probability from guesses   #
# - Desc		: A function that extracts information from guesses				 #
########################################################################
def get_list(words, guess, score):
	possible_words = []

	for word in words:
		maybe = collections.Counter(w for w, s in zip(word, score) if s != Let_Type.CORRECT)

		for word_char, guess_char, value in zip(word, guess, score):
			if word_char != guess_char and value == Let_Type.CORRECT:
				break
			elif word_char == guess_char and value != Let_Type.CORRECT:
				break
			elif value == Let_Type.PRESENT:
				if not maybe[guess_char]:
					break
				maybe[guess_char] -= 1
			elif value = Let_Type.INCORRECT and maybe[guess_char]:
				break
		else:
			possible_words.append(word)

	return possible_words

if __name__ == '__main__':
	with open(wordfile, "r") as file:
		wordlist = [word.strip for word in file.readlines()]

	option = input("Enter \"h\" for help or \"p\" to play: ")

	if option.strip.lower() == "h":
		print(help_text)
	else: 
		words = play(wordlist)