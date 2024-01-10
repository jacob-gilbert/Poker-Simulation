from collections import Counter
import deckOfCards

# class for each player's hand of cards from the deck
class hand(list): # a hand is a list of cards
    num_hands = 0 # this is for the number of hands
    values = [0,1,2,3,4,5,6,7,8,9,10,11,12] # these are possible values of the cards from two to ace

    # many values and lists that need initializing because of all the different types of hands a player can have
    def __init__(self, hand_of_cards):
        hand.num_hands += 1 # increase the number of hands by one
        self.dealt_list = []
        self.card_values = []
        self.append(hand_of_cards) # add the two cards the person is dealt to the hand
        self.royal_flush = False
        self.straight_flush = False
        self.quads = False
        self.quads_card = -1 # setting these to negative one because it will be useful for comparison, also a two is a 0 so we cannot use numbers 0-12 for initializing this
        self.full_house = False
        self.full_house_trips_card = -1
        self.full_house_pair_card = -1
        self.flush = False
        self.flush_hand = []
        self.flush_suit = -1
        self.flush_high_card = -1
        self.straight = False
        self.straight_high_card = -1
        self.straight_hand = []
        self.trips = False
        self.trips_card = -1
        self.two_pair = False
        self.two_pair_high_card = -1
        self.two_pair_low_card = -1
        self.pair = False
        self.pair_card = -1
        self.high_kicker = -1
        self.mid_kicker = -1
        self.low_kicker = -1
        self.dictSuits = {} # create a dictionary of all the suits that are in the hand
        self.highcard = -1

    # sorts the players hand given the deck being used and the player number
    def sort_hand(self, deck, hand_num):
        deck.sort_dealt() # sorts the deck
        self.dealt_list = deck.dealt[hand_num] # puts the sorted dealt cards from the deck into the hand's dealt_list
        return self 
    
    # grouping just the values of the cards
    def get_card_values(self):
        self.card_values = [card.value for card in self.dealt_list]

    # this calls all the functions that will be used to determines the quality of someone's hand
    def evaluate_hand(self):
        self.check_royal_flush()
        self.check_full_house()
        return
    
    # check if the hand contains a royal flush
    def check_royal_flush(self):
        self.check_straight_flush() # first check that there is a straight flush (if there is not straight flush there cannot be a royal flush)
        if self.straight_flush == True: # if there is a straight_flush determine if it is a royal flush
            if self.straight_hand[-1] == 12 and self.straight_hand[-2] == 11: # after calling check_straight_flush and a straight is found, those cards are put into a specific list, if the last card is an ace it is a royal flush because we have also verified it is a flush
                self.royal_flush = True
        return
    
    # check if there is a straight flush
    def check_straight_flush(self):
        self.check_flush() # check if there is a flush
        self.check_straight() # check if there is a straight
        if self.flush == True and self.straight == True: # if the hand has a straight and a flush then check if its the same five cards
            for i in range(len(self.flush_hand)):
                if self.straight_hand[i] in self.flush_hand: # check if every card in the straight is of the same suit
                    pass
                else:
                    return
            self.straight_flush = True # we only get to this point in the program if the above code passes every time, thus there is a straight flush
        return
    
    # check for a full house in the hand
    def check_full_house(self):
        self.check_pairs() # first check what kind of pairs the hand has
        if self.trips == True and self.pair == True: # a full house is made from a three of a kind and a pair, so if the hand has those two then it has a full house
            self.full_house_trips_card = self.trips_card
            self.full_house_pair_card = self.pair_card
            self.full_house = True
        return
    
    # check if a hand contains a flush
    def check_flush(self):
        for card in self.dealt_list: # going to go through every card in the hand
            if str(card.suit) not in self.dictSuits: # if the card's suit is not yet in the dictionary add it to the dictionary
                self.dictSuits[str(card.suit)] = 1
            else: # if the card's suit is already in the dictionary add 1 to the value of it
                self.dictSuits[str(card.suit)] += 1
        if "0" in self.dictSuits: # checks hearts
            if self.dictSuits["0"] >= 5: # if there are 5 or more hearts there is a flush so make the flush instance variable true
                self.flush = True
                self.flush_suit = 0
                for i in range(len(self.dealt_list)):
                    if self.dealt_list[-i - 1].suit == 0 and len(self.flush_hand) < 5: # appending the five highest cards in the flush to the flush_hand
                        self.flush_hand.append(self.card_values[-i - 1])
                self.flush_high_card = self.flush_hand[0] # highest value of the flush
                return
            if self.dictSuits["0"] >= 3: # the program only reaches this if there are less than 5 cards, if there are three to four cards with the same suit, but less than 5 than there cannot be a flush in the whole hand regardless of the other suits
                return
            
        # the code below is the same as the code above but changes the suit being considered
        if "1" in self.dictSuits: # checks spades
            if self.dictSuits["1"] >= 5:
                self.flush = True
                self.flush_suit = 1
                for i in range(len(self.dealt_list)):
                    if self.dealt_list[-i - 1].suit == 1 and len(self.flush_hand) < 5: # appending the five highest cards in the flush to the flush_hand
                        self.flush_hand.append(self.card_values[-i - 1])
                self.flush_high_card = self.flush_hand[0] # highest value of the flush
                return
            if self.dictSuits["1"] >= 3:
                return
        if "2" in self.dictSuits: # checks diamonds
            if self.dictSuits["2"] >= 5:
                self.flush = True
                self.flush_suit = 2
                for i in range(len(self.dealt_list)):
                    if self.dealt_list[-i - 1].suit == 2 and len(self.flush_hand) < 5: # appending the five highest cards in the flush to the flush_hand
                        self.flush_hand.append(self.card_values[-i - 1])
                self.flush_high_card = self.flush_hand[0] # highest value of the flush
                return
            if self.dictSuits["2"] >= 3:
                return
        if "3" in self.dictSuits: # check clubs
            if self.dictSuits["3"] >= 5:
                self.flush = True
                self.flush_suit = 3
                for i in range(len(self.dealt_list)):
                    if self.dealt_list[-i - 1].suit == 3 and len(self.flush_hand) < 5: # appending the five highest cards in the flush to the flush_hand
                        self.flush_hand.append(self.card_values[-i - 1])
                self.flush_high_card = self.flush_hand[0] # highest value of the flush
                return
            if self.dictSuits["3"] >= 3: #  and self.dictSuits["3"] < 5
                return
        return
    
    # check if the hand has a straight
    def check_straight(self):
        for start in range(len(self.card_values) - 4): # there are only 7 (index 0 to 6) cards in a hand so we only have to look at cards 0-4, 1-5, and 2-6
            if all(self.card_values[start] + i in self.card_values for i in range(5)): # if all the values in cards 0-4, 1-5, or 2-6 are increasing by 1 for every card then there is a straight
                self.straight = True
                self.highcard = False # since the player has a straight they are not playing a high card anymore
                self.straight_high_card = self.card_values[start] + 4 # record the highest value card of the straight in case that there is another straight, thus we can determine who wins by who has the "higher" straight
                self.straight_hand = [self.card_values[start] + i in self.card_values for i in range(5)]
            elif 12 in self.card_values and 0 in self.card_values and 1 in self.card_values and 2 in self.card_values and 3 in self.card_values: # this is a niche case of a straight that the previous if statement doesn't account for 
                self.straight = True
                self.highcard = False
                self.straight_high_card = 3
                self.straight_hand = [0, 1, 2, 3, 12]
        return
    
    # this assigns all values relating to quads
    def assign_quads(self, key):
        self.quads = True
        self.highcard = False # since the player has quads they are not playing a high card anymore
        self.quads_card = key
        for i in range(len(self.card_values)):
            if self.card_values[-i - 1] != self.quads:
                self.high_kicker = self.dealt_list[-i - 1] # determine the kicker, which is the highest value card not in the quads
                break
    
    # this assigns all values relating to trips
    def assign_trips(self, key):
        self.trips == True
        self.highcard = False # since the player has trips they are not playing a high card anymore
        self.trips_card = key
        kick_val_count = 0 # keep track of the number of kickers assigned because the first one should be the high and the second should be the low
        for i in range(len(self.card_values)):
            if self.card_values[-i - 1] != self.trips:
                if kick_val_count != 1:
                    self.high_kicker = self.card_values[-i - 1]
                else:
                    self.low_kicker = self.card_values[-i - 1]
                    break
    
    # this assigns all values relating to having a pair (note this function is only called when the hand does not have quads, trips, or two pair)
    def assign_pairs(self):
        kick_val_count = 0 # kicker counter
        for i in range(len(self.card_values)):
            if self.card_values[-i - 1] != self.pair_card: # only consider cards not in the pair
                if kick_val_count == 0:
                    self.high_kicker = self.card_values[-i - 1]
                    kick_val_count += 1
                elif kick_val_count == 1:
                    self.mid_kicker = self.card_values[-i - 1]
                    kick_val_count += 1
                elif kick_val_count == 2:
                    self.low_kicker = self.card_values[-i - 1]
                    kick_val_count += 1
        return

    # this assigns all values relating to having two pairs
    # note for there to be two pairs there must have first been a pair so all the self.pair information would have been assigned at this point so compare the new pair with the first pair
    def assign_two_pairs(self, key):
        if self.pair_card > key: # if the pair card is higher value than the key, the pair card is the higher value of the two pairs, and the key is the lower value of the two pairs
            self.two_pair_high_card = self.pair_card
            self.two_pair_low_card = key
        else: # the key is higher value than the pair card
            self.two_pair_high_card = key
            self.two_pair_low_card = self.pair_card
        for i in range(len(self.card_values)):
            if (self.card_values[-i - 1] != self.two_pair_low_card) and (self.card_values[-i - 1] != self.two_pair_high_card): # only consider cards not in the pairs for the kicker
                self.high_kicker = self.card_values[-i - 1]
                break
        return
    
    # this assigns all values relating to having three pairs
    # note for there to be three pairs there must have first been a pair and then two pairs, so all the relevant information for the first two pairs would have been assigned by now, so we compare the third pair with the first two
    def assign_three_pairs(self, key):
        if self.two_pair_low_card < key: # if the third pair is lower value than the already determined low value for the two pair, we no longer need to consider the third pair and are done
            if self.two_pair_high_card < key: # third pair is higher than the already determined high value pair so move the high to the low and the third to the high
                self.two_pair_low_card = self.two_pair_high_card
                self.two_pair_high_card = key
            else:
                self.two_pair_low_card = key # third pair is lower than the high pair but higher than the low pair so assign it to the low pair
            for i in range(len(self.card_values)):
                if self.card_values[-i - 1] != self.two_pair_low_card and self.card_values[-i - 1] != self.two_pair_high_card: # once again determine the kicker, it may have changed if different pairs are in the high and/or low spot now
                    self.high_kicker = self.card_values[-i - 1]
                    break
        return

    def check_pairs(self):
        count_values = Counter(self.card_values) # this looks that every card and counts how many of each value there are in the hand, so if there a three of a certain value the hand has trips
        pair_count = 0 # count the number of pairs, the most someone can have is 3, if that is the case then we must determine which pair not to use
        for key in count_values.keys(): # the keys are the specific card values in the hand
            if count_values[key] == 4: # check if a card value occurs four times
                self.assign_quads(key)
                break # if there are quads then we are done, 4 out of 5 cards are used so no room for another pair
            elif count_values[key] == 3: # check if a card value occurs three times
                self.assign_trips(key)
                # want to check if there is a pair here and there could be multiple so we will have to determine which is higher if there are multiple
                break
            elif count_values[key] == 2: # check if a card value occurs twice
                pair_count += 1
                self.pair = True
                self.highcard = False # since the player has at least a pair they are not playing a high card anymore
                if pair_count == 2:
                    self.two_pair = True
                    self.assign_two_pairs(key)
                elif pair_count == 3:
                    self.assign_three_pairs(key)
                    break
                else:
                    self.pair_card = key
        if self.quads == False and self.trips == False and self.two_pair == False:
            self.assign_pairs()
        return
    
    # compares two hands and returns the higher value one, returns -1 if its a tie
    def compare_hands(self, other_hand):

        # compare royal flush
        if self.royal_flush or other_hand.royal_flush: # if one or both of the hands have a royal flush
            if self.royal_flush and other_hand.royal_flush:
                return -1
            elif self.royal_flush:
                return self
            else:
                return other_hand
        
        # compare straight_flush
        if self.straight_flush or other_hand.straight_flush:
            if self.straight_flush and other_hand.straight_flush:
                if self.straight_high_card > other_hand.straight_high_card:
                    return self.straight_flush
                elif other_hand.straight_high_card > self.straight_high_card:
                    return other_hand.straight_flush
                else:
                    return -1
            elif self.straight_flush:
                return self
            else:
                return other_hand
                
        # compare quads
        if self.quads or other_hand.quads:
            if self.quads and other_hand.quads:
                if self.quads_card > other_hand.quads_card:
                    return self
                elif other_hand.quads_card > self.quads_card:
                    return other_hand
                else:
                    return -1
            elif self.quads:
                return self
            else:
                return other_hand
            
        # compare full house
        if self.full_house or other_hand.full_house:
            if self.full_house and other_hand.full_house:
                if self.full_house_trips_card == other_hand.full_house_trips_card:
                    if self.full_house_pair_card == other_hand.full_house_pair_card:
                        return -1
                    elif self.full_house_pair_card > other_hand.full_house_pair_card:
                        return self
                    else:
                        return other_hand
                elif self.full_house_trips_card > other_hand.full_house_trips_card:
                    return self
                else:
                    return other_hand
            elif self.full_house:
                return self
            else:
                other_hand.full_house
            
        # compare flush
        if self.flush or other_hand.flush:
            if self.flush and other_hand.flush:
                for i in range(len(self.flush_hand)):
                    if self.flush_hand[i] == other_hand.flush_hand[i]:
                        pass
                    if self.flush_hand[i] > other_hand.flush_hand[i]:
                        return self
                    else:
                        return other_hand
                return -1
            elif self.flush:
                return self
            else:
                return other_hand
            
        # compare straight
        if self.straight or other_hand.straight:
            if self.straight and other_hand.straight:
                if self.straight_high_card == other_hand.straight_high_card:
                    return -1
                elif self.straight_high_card > other_hand.straight_high_card:
                    return self
                else:
                    return other_hand
            elif self.straight:
                return self
            else:
                return other_hand
            
        # compare trips
        if self.trips or other_hand.trips:
            if self.trips and other_hand.trips:
                if self.trips_card == other_hand.trips_card:
                    if self.high_kicker == other_hand.high_kicker:
                        if self.low_kicker == other_hand.low_kicker:
                            return -1
                        elif self.low_kicker > other_hand.low_kicker:
                            return self
                        else:
                            return other_hand
                    elif self.high_kicker > other_hand.high_kicker:
                        return self
                    else:
                        return other_hand
                elif self.trips_card > other_hand.trips_card:
                    return self
                else:
                    return other_hand
            elif self.trips:
                return self
            else:
                return other_hand
            
        # compare two pair
        if self.two_pair or other_hand.two_pair:
            if self.two_pair and other_hand.two_pair:
                if self.two_pair_high_card == other_hand.two_pair_high_card:
                    if self.two_pair_low_card == other_hand.two_pair_low_card:
                        if self.high_kicker == other_hand.high_kicker:
                            return -1
                        elif self.high_kicker > other_hand.high_kicker:
                            return self
                        else:
                            return other_hand
                    elif self.two_pair_low_card > other_hand.two_pair_low_card:
                        return self
                    else:
                        return other_hand
                elif self.two_pair_high_card > other_hand.two_pair_high_card:
                    return self
                else:
                    return other_hand
            elif self.two_pair:
                return self
            else:
                return other_hand
            
        # compare pair
        if self.pair or other_hand.pair:
            if self.pair and other_hand.pair:
                if self.pair_card == other_hand.pair_card:
                    if self.high_kicker == other_hand.high_kicker:
                        if self.mid_kicker == other_hand.mid_kicker:
                            if self.low_kicker == other_hand.low_kicker:
                                return -1
                            elif self.low_kicker > other_hand.low_kicker:
                                return self
                            else:
                                return other_hand
                        elif self.mid_kicker > other_hand.mid_kicker:
                            return self
                        else:
                            return other_hand
                    elif self.high_kicker > other_hand.high_kicker:
                        return self
                    else:
                        return other_hand
                elif self.pair_card > other_hand.pair_card:
                    return self
                else:
                    return other_hand
            elif self.pair:
                return self
            else:
                return other_hand
            
        # compare kickers
        for i in range(5):
            if self.card_values[6 - i] == other_hand.card_values[6 - i]:
                pass
            elif self.card_values[6 - i] > other_hand.card_values[6 - i]:
                self.kicker = self.card_values[i]
                return self
            else:
                other_hand.kicker = other_hand.card_values[i]
                return other_hand
        # if the codes reaches this part the hands are tied
        return -1

        """if self.high_kicker == other_hand.high_kicker:
            if self.mid_kicker == other_hand.mid_kicker:
                if self.low_kicker == other_hand.low_kicker:
                    return -1
                elif self.low_kicker > other_hand.low_kicker:
                    return self
                else:
                    return other_hand
            elif self.mid_kicker > other_hand.mid_kicker:
                return self
            else:
                return other_hand
        elif self.high_kicker > other_hand.high_kicker:
            return self
        else:
            return other_hand"""
            
    def print_winner(self):
        if self.royal_flush:
            print("with a royal flush")
        elif self.straight_flush:
            print("with a straight flush")
        elif self.quads:
            print("with quads")
        elif self.full_house:
            print("with a full hosue")
        elif self.flush:
            print("with a flush")
        elif self.straight:
            print("with a straight")
        elif self.trips:
            print("with trips")
        elif self.two_pair:
            print("with two pair")
        elif self.pair:
            print("with a pair")
        else:
            print("with kickers:", self.card_values[6] + 2, ",", self.card_values[5] + 2, ",", self.card_values[4] + 2, ",", self.card_values[3] + 2, ",", self.card_values[2] + 2)
