word_len = int(input("Enter the length of the words to be extracted: "))

input_f = "words_alpha.txt"
output_f = "wordle-words.txt"

with open(input_f, "r") as input:
	with open(output_f, "w") as output:
		wordlist = input.readlines()
		for word in wordlist:
			word = word.rstrip()
			if len(word) == word_len:
				 output.write(word+"\n")


print("\nDone :)")