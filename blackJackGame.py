import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def generate_cards(list_cards):
    cards_list=[]
    for i in range(2):
        cards_list.append(random.choice(list_cards))
    return cards_list
def sum_cards(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1  
        total = sum(hand)  
    return total
def add_one_card(list_cards,ass_crds):
    ass_crds.append(random.choice(list_cards))
    return ass_crds

def computer_turn(computer_cards,list_cards):
    while sum_cards(computer_cards)<17:
        add_one_card(list_cards,computer_cards)
    return computer_cards


while True:
    ans = input(("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
    if ans == 'y':
        user_cards = generate_cards(cards)
        computer_cards = generate_cards(cards)
        print(f"Your cards: {user_cards}")
        print(f"Computer first card: {computer_cards[0]}")
        while True:
            user_total = sum_cards(user_cards)
            if user_total > 21:
                print(f"You Lose! Your total score is: {user_total}")
                break
            ans_user = input(("Type 'y' to get another card, type 'n' to pass: ")).lower()
            if ans_user == 'y':
                add_one_card(cards,user_cards)
                print(f"Your cards: {user_cards}")
            elif ans_user == 'n':
                print(f"Your final hand is {user_cards}, and you total score is: {user_total}")
                break
        if user_total<=21:
            computer_turn(computer_cards,cards)
            computer_total = sum_cards(computer_cards)
            print(f"Computer final hand {computer_cards}, and his score is: {computer_total}")

            if computer_total>21 or user_total>computer_total:
                print("You win!")
            elif computer_total > user_total:
                print("You Lose!")
            else:
                print("It's a Draw")
    else:
        print("Good Bye!")
        break
