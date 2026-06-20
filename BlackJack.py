import random
import time

suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

values = {
    "A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10
}

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

deck = create_deck()

def draw_card():
    global deck
    if not deck:
        deck = create_deck()
    return deck.pop()

def hand_value(hand):
    total = sum(values[rank] for rank, suit in hand)
    aces = sum(1 for rank, suit in hand if rank == "A")

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def deal_hand():
    return [draw_card(), draw_card()]

def print_cards(hand):
    lines = ["", "", "", "", ""]

    for rank, suit in hand:
        r = rank if len(rank) == 2 else rank + " "

        lines[0] += "┌─────┐ "
        lines[1] += f"│{r}   │ "
        lines[2] += f"│  {suit}  │ "
        lines[3] += f"│   {r[::-1]}│ "
        lines[4] += "└─────┘ "

    for line in lines:
        print(line)

def print_hidden_dealer(hand):
    lines = ["", "", "", "", ""]

    first = hand[0]
    r = first[0] if len(first[0]) == 2 else first[0] + " "

    lines[0] += "┌─────┐ "
    lines[1] += f"│{r}   │ "
    lines[2] += f"│  {first[1]}  │ "
    lines[3] += f"│   {r[::-1]}│ "
    lines[4] += "└─────┘ "

    lines[0] += "┌─────┐ "
    lines[1] += "│░░░░░│ "
    lines[2] += "│░░░░░│ "
    lines[3] += "│░░░░░│ "
    lines[4] += "└─────┘ "

    for line in lines:
        print(line)

def player_turn(name):
    print(f"\n=== {name}'s Turn ===")
    time.sleep(1.5)

    hand = deal_hand()
    count = hand_value(hand)

    print_cards(hand)
    time.sleep(1.2)
    print("\nTotal:", count)
    time.sleep(1.5)

    while count < 21:
        choice = input("\nTwist or Hold? ").strip().lower()

        if choice == "hold":
            break

        if choice == "twist":
            hand.append(draw_card())
            time.sleep(1)

            print()
            print_cards(hand)
            time.sleep(1.2)

            count = hand_value(hand)
            print("\nTotal:", count)
            time.sleep(1.5)

            if count > 21:
                print("\nBUST!")
                break
        else:
            print("Type Twist or Hold.")

    if count == 21:
        print("\nBlackjack!")

    return hand, count

print("=== BLACKJACK ===")
print("1. Single Player vs Dealer")
print("2. Player vs Player")

while True:
    mode = input("\nChoose mode (1 or 2): ").strip()
    if mode in ("1", "2"):
        break

if mode == "1":

    print("\n=== Dealer deals first ===")
    time.sleep(1.5)

    dealer_hand = deal_hand()
    dealer_count = hand_value(dealer_hand)

    print("Dealer shows:")
    print_hidden_dealer(dealer_hand)
    time.sleep(2)

    if dealer_count == 21:
        print("\nDealer Blackjack!")
        print_cards(dealer_hand)
        exit()

    print("\nYour turn...")
    time.sleep(1.5)

    player_hand, player_count = player_turn("Player")

    print("\n=== Dealer reveals ===")
    time.sleep(2)

    print_cards(dealer_hand)
    print("\nTotal:", dealer_count)

    while dealer_count < 17:
        print("\nDealer draws...")
        time.sleep(1.5)

        dealer_hand.append(draw_card())
        dealer_count = hand_value(dealer_hand)

        print_cards(dealer_hand)
        print("\nTotal:", dealer_count)

        time.sleep(2)

    print("\n=== Final Results ===")

    print("\nPlayer:")
    print_cards(player_hand)
    print("Total:", player_count)

    print("\nDealer:")
    print_cards(dealer_hand)
    print("Total:", dealer_count)

    if player_count > 21:
        print("\nDealer wins!")
    elif dealer_count > 21:
        print("\nDealer busts! You win!")
    elif player_count > dealer_count:
        print("\nYou win!")
    elif player_count < dealer_count:
        print("\nDealer wins!")
    else:
        print("\nTie!")

else:

    print("\n=== PLAYER VS PLAYER (NO DEALER) ===")
    time.sleep(1.5)

    print("\nPlayer 1 turn...")
    player1_hand, player1_count = player_turn("Player 1")

    print("\n" + "=" * 40)
    input("Pass to Player 2 and press Enter...")
    print("=" * 40)

    player2_hand, player2_count = player_turn("Player 2")

    print("\n=== FINAL RESULTS ===")

    print("\nPlayer 1:")
    print_cards(player1_hand)
    print("Total:", player1_count)

    print("\nPlayer 2:")
    print_cards(player2_hand)
    print("Total:", player2_count)

    if player1_count > 21 and player2_count > 21:
        print("\nBoth busted!")
    elif player1_count > 21:
        print("\nPlayer 2 wins!")
    elif player2_count > 21:
        print("\nPlayer 1 wins!")
    elif player1_count > player2_count:
        print("\nPlayer 1 wins!")
    elif player2_count > player1_count:
        print("\nPlayer 2 wins!")
    else:
        print("\nTie!")