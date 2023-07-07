# Card Race Simulation
A simulation of a card race betting game, to see how variations in the deck effect the probability of a certain suit winning.

## How the game works
Firstly the ace cards are removed from the deck and placed in a line.

Then, a length for the race is chosen (k_length_of_line) and that many cards are removed
and placed face down in a vertical line above the aces.

Then a card is taken from the top of the deck, the ace of the revealed card's suit is moved up one space.
When all of the aces are part a certain position, the card in that vertical space is revealed and the ace
of the revealed card's suit is moved back one space.

Whichever suit is the first to get to the final row is the winner.


This can be played as a drinking game by betting sips on a suit, when a suit wins the people that bet on that
suit can allocate the other players to drink the total number of sips that were bet on all four suits.

## Installation

### Creating a Virtual Environment
Virtual Environments (venvs) are used to isolate requirements for different python projects across your OS. For more
information see [official documentation](https://docs.python.org/3/library/venv.html).

Create a venv using:

```commandline

python -m venv venv

```


Activate it using:

```commandline

source venv/bin/activate

```

### Dependencies
Once in a virtual environment (or globally, if you want) you can install the dependencies for this project by using this
command at the project root folder:

```commandline
pip install -r requirements.txt
```

This will install the following python packages:
* [tqdm](https://github.com/tqdm/tqdm) - Provides a progress bar for running multiple games at once

## Setting parameters
Parameters for how the game are run can be found and tweaked in [constants.py](simulator/constants.py).

The parameters are:
* k_length_of_line - The number of spaces in the line that the aces need to get through to win
* k_extra_cards - A dictionary defining how many cards to add/remove of each suit in the initial deck

## How to run the program

### Single Game
To run a single game with full verbose output, set the [parameters](#setting-parameters) appropriately, run the
following command at the root of the project:
```commandline
python -m simulator.single_game
```
Warning: If the deck in the game runs out of cards the error `IndexError: pop from empty list` will be raised.


### Multiple Games
To run multiple games and get the probability of the deck emptying and each suit winning, set the
[parameters](#setting-parameters) appropriately and run the following command at the root of the project:
```commandline
python -m simulator.multiple_games
```


## How to run tests
To run tests, execute the following command at the root of the project:
```commandline
python -m unittest discover -s tests
```


## TODO
Here is a list of planned / potential features to implement:
* A way of storing the array of wins that is a result of multiple_games.py, this would allow processing the information
to find facts like the longest unbroken run of one suit winning
* Find a better way of representing cards with value 10 as a string, instead of using three characters
* Implementing the more efficient algorithm for adding/removing extra cards of each suit in deck.py
* Implementing a custom error for when the deck runs out of cards, instead of the current method using IndexError which 
is too generic
* Add a test to check that the deck is shuffled correctly by the GameState class
* Add tests for the multiple_games and single_game files
