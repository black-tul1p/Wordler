#! /usr/bin/python3

# Author: black-tul1p

#############################  IMPORTS  ################################
import enum, random, collections

#############################  CLASSES  ################################

class Let_Type(enum.Enum):
	INCORRECT = 0
	PRESENT 	= 1
	CORRECT 	= 2

############################ GLOBAL VARS  ##############################
wordfile  = "wordle_words.txt"
wordlist  = []
guesses   = []
probs     = []
letters   = []
guess_num = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
not_gameover    = False

help_text = '''
______________________________________________
Format for entering score for the guess:
  -> #####

Example: 00201

Probability values for #:
  -> 0 : Incorrect
  -> 1 : Wrong Position
  -> 2 : Correct
______________________________________________
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

	# Calculate score for guess against word
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
# - Inputs  : List of possible words																   #
# - Outputs : Final list of words																		   #
# - Desc		: A function that takes user input for guesses in a loop 	 #
########################################################################
def play(wordlist):
	counter = 0
	while len(wordlist) > 1:
		guess = get_word(wordlist)
		mapping = {"0": Let_Type.INCORRECT, "1": Let_Type.PRESENT, "2": Let_Type.CORRECT}

		# Get and store guess in array
		score = ""
		while len(score) != 5:
			score = input("Score for the "+ guess_num[counter]+ " guess (or \"h\" for help): ")
			if score.strip().lower() == "h":
				print(help_text)
			else:
				if len(score) != 5 and not score.isnum():
					print("[X] Please enter the score in the correct format\n")
		if score == "22222":
			print("\nTurns out the odds were in your favor after all.")
			not_gameover = True
			return [guess]
		score_array = [mapping[char] for char in score if char in mapping]
		wordlist = update_list(wordlist, guess, score_array)
		print()
		counter += 1
	
	return wordlist


##############################  FUNCTION  ##############################
# - Inputs  : The user-entered guess string													   #
# - Outputs : Arrays containing letters and probability from guesses   #
# - Desc		: A function that extracts information from guesses				 #
########################################################################
def get_word(wordlist):
	print(f"I foresee {len(wordlist)} possibilities...")
	sample = ", ".join(words[:24])
	print(f"Some of which include {sample}.")
	guess = random.choice(wordlist)
	print(f"Tempt fate with {guess!r}...\n")
	return guess


##############################  FUNCTION  ##############################
# - Inputs  : The user-entered guess string													   #
# - Outputs : Arrays containing letters and probability from guesses   #
# - Desc		: A function that extracts information from guesses				 #
########################################################################
def update_list(words, guess, score):
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
			elif value == Let_Type.INCORRECT and maybe[guess_char]:
				break
		else:
			possible_words.append(word)

	return possible_words


############################ MAIN FUNCTION  ############################

if __name__ == '__main__':
	with open(wordfile, "r") as file:
		wordlist = [word.strip().upper() for word in file.readlines()]

	option = input("Enter \"h\" for help or \"p\" to play: ")
	print()

	if option.strip().lower() == "h":
		print(help_text)
	else: 
		words = play(wordlist)

	if not_gameover:
		if not words:
			raise RuntimeError("No words can save you now.")
		if not words[0]:
			print(f"Only a miracle can save you now.")
		else:
			print(f"The only word that can end this is {words[0]!r}.")

########################################################################