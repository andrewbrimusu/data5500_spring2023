from DeckOfCards import DeckOfCards

# import DeckOfCards

deck = DeckOfCards()

deck.print_deck()

deck.shuffle_deck()

deck.print_deck()


# deal two cards to the user
card = deck.get_card()
card2 = deck.get_card()

print(card)
print(card2)

score = 0
# calculate the user's hand score
score += card.val
score += card2.val
print("Your score is: ", score)


# ask user if they would like a "hit" (another card)
hit = input("would you like a hit? ")

while hit == 'y':
    card3 = deck.get_card()
    print(card3)
    
    score += card3.val
    print("new score: ", score)
    
    if score > 21:
        print("you lose!!!!")
        
    hit = input("would you like another hit? ")
