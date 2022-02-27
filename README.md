<p align="center"> <img src="https://github.com/black-tul1p/wordler/blob/main/Images/logo.png" width="250" /> </p> <hr>

A [Wordle](https://www.nytimes.com/games/wordle/index.html) solver implemented in Python 🐍

<div align="center">
	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Wordle_196_example.svg/1200px-Wordle_196_example.svg.png" width="500" />
	<p align="center">
		<sub>
			Why did I decide to ruin the fun of the game? For <i>fun</i> of course (and to see if I could 😋)
		</sub>
	</p>
</div>

## How does it work? 🤔

This implementation is pretty intuitive, no fancy graph or path-finding algorithms were required to determine the most likely word, thanks to **dynamic programming** (through the use of a cached wordlist). 

The code begins by suggesting a word containing the _most mathematically likely_ word with completely unique (non-repeating) characters, `RAISE`, to greatly narrow the list of possibilities **from thousands of words to tens of words!** . In the second iteration, the code creates a list of words from the original (unaltered) wordlist using the following rules:
> The word contains none of the characters in the first guess

> The word contains purely unique characters

This allows us to try out a total of 10 unique characters in the first two tries, so that we can narrow down the cached wordlist as much as possible. In future tries, the code suggests a random word from the cached wordlist each iteration, after which the wordlist is updated to get rid of unlikely words. 

The elimination of words in every iteration is performed using a scoring mechanism. The scores are as follows:
<p align="center"> <img src="https://github.com/black-tul1p/wordler/blob/main/Images/Explanation_1.png" width="300" /> </p>

Each word in the cached wordlist is scored against the guess and is not removed ***if and only if*** it satisfies all of the following:
> It does not contain any absent characters

> It contains the correct characters in the right positions 

> It contains the present characters in a different position

<p align="center"> <img src="https://github.com/black-tul1p/wordler/blob/main/Images/Explanation_2.png" width="300" /> </p>

All words that do not fit this criteria are *removed* from the cached wordlist. This narrows down the list of possibilities each iteration and, on average, solves the wordle in **3-ish tries**! 

## Example Run 🎮
```python
$ ./wordler.py

Start by tempting fate with 'RAISE'...

Enter a custom guess or score (or "h" for help): 00210

Next, tempt fate with 'FLOWN'...

Enter a custom guess or score (or "h" for help): 01000

I foresee 5 possibilities...
Tempt fate with 'SPILL'...

Enter a custom guess or score (or "h" for help): 22222

Turns out the odds were in your favor after all.
```
<div align="center">
	<img src="https://github.com/black-tul1p/wordler/blob/main/Images/solve.png" width="400" />
	<p align="center">
		<sub>
			Correct on the 3rd try? Pretty good! 🤑
		</sub>
	</p>
</div>

## Requirements ⚒️
You need `python3` and the following packages:
```
enum, random, collections
```

**Note**: You can install a package by running `pip3 install [package-name]`

## Usage 🕹️
Clone this repo by running: `git clone https://github.com/black-tul1p/wordler.git`

Run the program after `cd`-ing into the cloned directory by running: `./wordler.py` or `python3 wordler.py`

<hr>
<p> <b>Note:</b> This program uses the wordlist from <a href="https://github.com/csokolove/wordle-word-list/blob/main/wordlist.csv">csokolove/wordle-word-list</a>. </p>
<p> Thanks to <a href = "https://medium.com/@tglaiel/the-mathematically-optimal-first-guess-in-wordle-cbcb03c19b0a">Tyler Glaiel</a> for figuring out the most mathematically likely word with non-repeating characters.</p> 

