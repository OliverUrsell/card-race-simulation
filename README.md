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

[//]: # (## Installation)

[//]: # (### Creating a venv)

[//]: # (Create a venv using:)

[//]: # (```commandline)

[//]: # (python -m venv venv)

[//]: # (```)

[//]: # ()
[//]: # (Activate it using:)

[//]: # (```commandline)

[//]: # (source venv/bin/activate)

[//]: # (```)

[//]: # (### Dependencies)

## Setting parameters
Parameters for how the game are run can be found and tweaked in [constants.py](simulator/constants.py).

The parameters are:
* k_length_of_line - The number of spaces in the line that the aces need to get through to win
* k_extra_cards - A dictionary defining how many cards to add/remove of each suit in the initial deck

## How to run the program
To run a single game with full verbose output, run the following command at the root of the project:
```commandline
python -m simulator.single_game
```
Warning: If the deck in the game runs out of cards the error `IndexError: pop from empty list` will be raised.

## How to run tests
To run tests, execute the following command at the root of the project:
```commandline
python -m unittest discover -s tests
```
