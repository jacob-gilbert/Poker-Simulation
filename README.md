# Texas Hold-Em Poker Simulation in Python

## Simulates a three handed game of Texas Hold-Em Poker, showing which hand won and how it won.

In order to simulate the game the following classes were created:
* card class: with the help of enums cards are assigned a suit and a value
* deckOfCards class: every deck consists of 52 cards (4 suits and 13 different values per suit) and each deck must be shuffled and dealt
* hand class: after all the cards are dealt hands must be evaluated to determine the value of each hand and then compared to determine the winner
* playPoker class: this is where all the shuffling and dealing take place as well as the calls for evaluation and comparison of the hands

This simulation does not use complex techniques and just follows the basic logic associated with Texas Hold-Em poker using for loops, while loops, and if statements.
All you have to do is run the code and tell it how many players there are and it will simulate the game.

Made with Python 3.9.12

## Known Issues (work in progress)
* Only works for three players
* Doesn't display the value of what won, so it can tell you that a flush won, but it won't tell the cards that make up the flush, or the value of a pair that won and with what kicker
