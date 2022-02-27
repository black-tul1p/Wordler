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

This implementation is pretty intuitive, no fancy graph or path-finding algorithms were required to determine the most likely word, thanks to dynamic programming. The code begins by suggesting a word containing the most mathematically likely unique characters, `RAISE`, to greatly narrow the updated wordlist.

In the next iteration, the code creates a list of words from the original (unaltered) wordlist using the following rules:
> The word contains none of the characters in the first guess

> The word contains purely unique characters

This allows us to try out a total of 10 unique characters in the first two tries, so that we can narrow down the updated wordlist as much as possible.

In the further iterations, the code simply suggests a random word from the updated wordlist each iteration, after which the wordlist is updated to get rid of unlikely words. The elimination of words is performed using a scoring mechanism.

The scores are as follows:
<p align="center"> <img src="https://github.com/black-tul1p/wordler/blob/main/Images/Explanation_1.png" width="300" /> </p>

Each word in the wordlist is scored against the guess and are added to the updated wordlist **if and only if** they do not contain absent characters, contain the correct characters in the right places and contain the present characters in a different place.

<p align="center"> <img src="https://github.com/black-tul1p/wordler/blob/main/Images/Explanation_2.png" width="300" /> </p>

This narrows down the list of possibilities each iteration and, on average, solves the wordle in 3-4 tries! 

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
<b>Note:</b> This program uses the wordlist from <a href="https://github.com/csokolove/wordle-word-list/blob/main/wordlist.csv">csokolove/wordle-word-list</a>.
