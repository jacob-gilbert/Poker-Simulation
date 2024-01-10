from enum import Enum, auto

class cardVals(Enum):
    Two = 0
    Three = 1
    Four = 2
    Five = 3
    Six = auto()
    Seven = auto()
    Eight = auto()
    Nine = auto()
    Ten = auto()
    Jack = auto()
    Queen = auto()
    King = auto()
    Ace = auto()

# Map 0-3 to suits
class cardSuits(Enum):
    Hearts = 0
    Spades = 1
    Diamonds = 2
    Clubs = 3

# class for an individual card
class card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{cardVals(self.value).name} of {cardSuits(self.suit).name}"