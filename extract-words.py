#! /usr/bin/python3

########################### HELPER FUNCTIONS  ##########################

def read_wordlist(input_f):
	wordlist = []
	with open(input_f, "r") as input:
		wordlist = input.readlines()
	return wordlist

def write_wordlist(output_f, list, n):
	with open(output_f, "w") as output:
		for word in list:
			word = word.rstrip()
			if len(word) == n:
				output.write(word+"\n")

########################################################################


############################ MAIN FUNCTION  ############################

if __name__ == '__main__':
	input_f = "wordle_words.txt"
	output_f = "wordle_words2.txt"
	word_len = int(input("Enter the length of the words to be extracted: "))

	wordlist = read_wordlist(input_f)
	wordlist.sort()

	write_wordlist(output_f, wordlist, word_len)

	print("\nDone :)")

########################################################################