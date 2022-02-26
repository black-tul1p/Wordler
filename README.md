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

This implementation is pretty intuitive, no fancy graph or path-finding algorithms were used to determine the most likely word. The code simply suggests a random word from the wordlist each iteration, after which the wordlist is updated to get rid of unlikely words. The elimination of words is performed using a scoring mechanism. 

The scores are as follows:
<p align="center"> <img src="https://github.com/black-tul1p/wordler/blob/main/Images/Explanation_1.png" width="300" /> </p>

Each word in the wordlist is scored against the guess and are added to the updated wordlist **if and only if** they do not contain absent characters, contain the correct characters in the right places and contain the present characters in a different place.

<p align="center"> <img src="https://github.com/black-tul1p/wordler/blob/main/Images/Explanation_2.png" width="300" /> </p>

This narrows down the list of possibilities each iteration and, on average, solves the wordle in 4<i>-ish</i> tries! 

## Example Run 🎮
```python
$ ./wordler.py

Enter "h" for help or [ENTER] to play:

I foresee 2315 possibilities...
Some of which include ABACK, ABASE, ABATE, ABBEY, ABBOT, ABHOR, ABIDE, ABLED, ABODE, ABORT, ABOUT, ABOVE, ABUSE, ABYSS, ACORN, ACRID, ACTOR, ACUTE, ADAGE, ADAPT, ADEPT, ADMIN, ADMIT, ADOBE.
Tempt fate with 'DROOL'...

Enter a custom guess or score (or "h" for help): IRATE
Enter the score: 10000

I foresee 130 possibilities...
Some of which include BIDDY, BILLY, BINGO, BISON, BLIMP, BLIND, BLINK, BLISS, BUILD, CHICK, CHILD, CHILI, CHILL, CINCH, CIVIC, CIVIL, CLICK, CLIFF, CLIMB, CLING, CLINK, COMIC, CONIC, CUBIC.
Tempt fate with 'SPICY'...

Enter a custom guess or score (or "h" for help): 00100

I foresee 16 possibilities...
Some of which include BINGO, DINGO, FLUID, FOLIO, FUNGI, HUMID, LIMBO, LINGO, LIVID, LOGIN, MINIM, OVOID, UNDID, VIGIL, VIVID, WIDOW.
Tempt fate with 'LINGO'...

Enter a custom guess or score (or "h" for help): 02000

The only word that can end this is 'VIVID'.
```
<div align="center">
	<img src="https://github.com/black-tul1p/wordler/blob/main/Images/solve.png" width="400" />
	<p align="center">
		<sub>
			Correct on the 4th try? Not bad 🙃
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
