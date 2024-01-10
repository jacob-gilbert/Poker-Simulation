import card
import random

# class for a deck of cards
class deckOfCards(list):
    # initialize a deck of cards
    def __init__(self):
        suits = list(range(4)) # 4 suits mapped 0-3
        values = list(range(13)) # 13 cards (2 to A) mapped 0-12
        [[self.append(card.card(i,j)) for j in suits] for i in values] # create 52 instances of card that are all unique like a hand of cards
        self.dealt = [] # this list will be filled with everyone's hands, when flop, turn, river are played they will be added to each hand
    
    # randomize the deck so that the order is unknown
    def shuffle(self):
        random.shuffle(self) # randomizes deck
        print("Deck Shuffled:")

    # deals players
    def dealPlayer(self):
        self.dealt.append([self[0],self[1]]) # add top two cards to the deck in a list (since its in the list)
        return [self.pop(0), self.pop(0)]
    
    # burns a card by removing it from the deck
    def burn(self):
        self.pop(0)

    # plays the flop
    def flop(self, handCount):
        flopList = [self.pop(0), self.pop(0), self.pop(0)] # removes the top three cards from the deck and puts them into their own list
        for i in range(handCount):
            self.dealt[i].extend(flopList) # adds the flop to each player's hand in the dealt list
        print("Flop revealed: " + str(flopList[0]) + ",", str(flopList[1]) + ",", flopList[2]) # prints out the flop

    # plays the turn
    def turn(self, handCount):
        turnList = [self.pop(0)] # removes the top card from the deck
        for i in range(handCount):
            self.dealt[i].extend(turnList) # adds the turn to each player's hand in the dealt list
        print("Turn Revealed:", turnList[0]) # prints out the turn

    # plays the river
    def river(self, handCount):
        riverList = [self.pop(0)] # removes the top card from the deck
        for i in range(handCount):
            self.dealt[i].extend(riverList) # adds the river to each player's hand in the dealt list
        print("River Revealed:", riverList[0]) # prints out the river

    # this sorts the dealt list using selection sort (hands are small so this should not be a problem) 
    # sorting the dealt list will make it easier to find the kickers
    def sort_dealt(self):
        for i in range(len(self.dealt)): # dealt_list is a list of lists where the inner lists are the players hands, so we look at each person's hand one at a time
            curr_list = self.dealt[i] # this keeps track of the current hand we are looking at
            for j in range(len(curr_list)): # selection sort
                lowest = curr_list[j]
                for k in range(j + 1,len(curr_list)):
                    if lowest.value > curr_list[k].value: # putting smallest values first (we do not care about suits for this)
                        temp = lowest
                        curr_list[j] = curr_list[k]
                        lowest = curr_list[k]
                        curr_list[k] = temp
        return