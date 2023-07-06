# Card Race Simulation
A simulation of a card race betting game, to see how variations in the deck effect the probability of a certain suit winning.

## How the game works

## Installation
### Creating a venv
Create a venv using:
```commandline
python -m venv venv
```

Activate it using:
```commandline
source venv/bin/activate
```

### Dependencies

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
