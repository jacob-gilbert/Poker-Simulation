import card
import deckOfCards
import hand

deck = deckOfCards.deckOfCards()
deck.shuffle()

# as of right now it only works with three players
numOfPlayers = int(input("How many players are there? "))
while numOfPlayers != 3:
    numOfPlayers = int(input("How many players are there? "))

hand1 = hand.hand(deck.dealPlayer())
print("Hand 1: " + str(hand1[0][0]) + ",", hand1[0][1])

hand2 = hand.hand(deck.dealPlayer())
print("Hand 2: " + str(hand2[0][0]) + ",", hand2[0][1])

hand3 = hand.hand(deck.dealPlayer())
print("Hand 3: " + str(hand3[0][0]) + ",", hand3[0][1])


# deal the rest of the cards
deck.burn()

deck.flop(hand.hand.num_hands)

deck.burn()

deck.turn(hand.hand.num_hands)

deck.burn()

deck.turn(hand.hand.num_hands)

deck.sort_dealt()

# problems here
hand1.sort_hand(deck, 0)
hand1.get_card_values()

hand2.sort_hand(deck, 1)
hand2.get_card_values()

hand3.sort_hand(deck, 2)
hand3.get_card_values()

hand1.evaluate_hand()
hand2.evaluate_hand()
hand3.evaluate_hand()


# determine who wins
winner1 = hand1.compare_hands(hand2)
if winner1 != -1:
    winner2 = winner1.compare_hands(hand3)
    if winner2 == -1:
        if winner1 == hand1:
            print("Hand1 and Hand2 tie")
            winner1.print_winner()
        if winner1 == hand2:
            print("Hand2 and Hand3 tie")
            winner1.print_winner()
    elif winner2 == hand1:
        print("Hand1 wins")
        winner2.print_winner()
    elif winner2 == hand2:
        print("Hand2 wins")
        winner2.print_winner()
    else:
        print("Hand3 wins")
        winner2.print_winner()
else:
    winner1 = hand1.compare_hands(hand3)
    if winner1 == -1:
        print("All hands tie")
    elif winner1 == hand1:
        print("Hand1 and Hand2 tie")
        winner1.print_winner()
    elif winner1 == hand2:
        print("Hand1 and Hand2 tie")
        winner1.print_winner()
    else:
        print("Hand3 wins")
        winner1.print_winner()