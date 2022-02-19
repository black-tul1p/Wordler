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
import re

############################ GLOBAL VARS  ##############################
guesses   = []
probs     = []
letters   = []
guess_num = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
chars     = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
				'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
					'v', 'w', 'x', 'y', 'z']

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
# - Inputs  : None													   #
# - Outputs : None													   #
# - Desc	: A function that takes user input for guesses in a loop   #
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

		# Remove unneeded characters
		update_charlist(curr_probs, curr_chars)

		print()
		#print(guesses)

##############################  FUNCTION  ##############################
# - Inputs  : The user-entered guess string							   #
# - Outputs : Arrays containing letters and probability from guesses   #
# - Desc	: A function that extracts information from guesses		   #
########################################################################
def extract_info(guess):
	curr_lett = []
	curr_prob = []
	for i in range(len(guess)):
		if (i+1) % 2 != 0:
			curr_lett.append(guess[i])
		else:
			curr_prob.append(guess[i])	
	letters.append(curr_lett)
	probs.append(curr_prob)
	return curr_prob, curr_lett

##############################  FUNCTION  ##############################
# - Inputs  : Arrays containing letters and probability from guesses   #
# - Outputs : None													   #
# - Desc	: A function that removes invalid letters from chars[]	   #
########################################################################
def update_charlist(probs_arr, lett_arr):
	for i in range(len(probs_arr)):
		if int(probs_arr[i]) == 0:
			chars.remove(lett_arr[i]) 

##############################  FUNCTION  ##############################
# - Inputs  : Arrays containing letters and probability from guesses   #
# - Outputs : Regex string 											   #
# - Desc	: A function that creates a regex string to match words	   #
########################################################################
def create_regex(probs_arr, lett_arr):
	for i in range(len(lett_arr)):

if __name__ == '__main__':
	print(help_text)
	guess_loop()
	extract_info()