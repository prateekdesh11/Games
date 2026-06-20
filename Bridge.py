import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

players = ["North", "East", "South", "West"]

hands = {
    "North": sorted(deck[0:13], key=lambda x: (x[1], ranks.index(x[0]))),
    "East": sorted(deck[13:26], key=lambda x: (x[1], ranks.index(x[0]))),
    "South": sorted(deck[26:39], key=lambda x: (x[1], ranks.index(x[0]))),
    "West": sorted(deck[39:52], key=lambda x: (x[1], ranks.index(x[0])))
}

tricks = {p: 0 for p in players}

def card_value(card):
    return ranks.index(card[0])

def show_hand(hand):
    for i, card in enumerate(hand):
        print(f"{i}: {card[0]} of {card[1]}")

leader = 0

print("\nYou are SOUTH\n")

for trick in range(13):

    print(f"\n=== Trick {trick+1} ===")

    played = {}
    lead_suit = None

    order = players[leader:] + players[:leader]

    for player in order:

        hand = hands[player]

        if player == "South":

            print("\nYour hand:")
            show_hand(hand)

            while True:
                try:
                    choice = int(input("Choose card number: "))
                    if 0 <= choice < len(hand):
                        card = hand[choice]

                        if lead_suit and card[1] != lead_suit:
                            if any(c[1] == lead_suit for c in hand):
                                print("You must follow suit!")
                                continue

                        break
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Enter a number.")

            card = hand.pop(choice)

        else:

            valid_cards = hand

            if lead_suit:
                suit_cards = [c for c in hand if c[1] == lead_suit]
                if suit_cards:
                    valid_cards = suit_cards

            card = random.choice(valid_cards)
            hand.remove(card)

        if lead_suit is None:
            lead_suit = card[1]

        played[player] = card
        print(f"{player} plays {card[0]} of {card[1]}")

    winner = None
    best_value = -1

    for player, card in played.items():
        if card[1] == lead_suit and card_value(card) > best_value:
            best_value = card_value(card)
            winner = player

    tricks[winner] += 1
    leader = players.index(winner)

    print(f"\n{winner} wins the trick!")

print("\nFinal Tricks:")

for p in players:
    print(p, tricks[p])