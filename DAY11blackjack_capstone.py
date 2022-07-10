# my solution
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []


def give_user_cards():
    for i in range(0,2):
        card = random.choice(cards)
        user_cards.append(card)

def give_computer_cards():
    for i in range(0,2):
        card = random.choice(cards)
        dealer_cards.append(card)

def hit_me():
    card = random.choice(cards)
    user_cards.append(card)

def add_score(list) -> int:
    summation = 0
    for i in list:
        summation += i
    return summation

def clear_cards():
    user_cards.clear()
    dealer_cards.clear()

def deal_cards():
    give_user_cards()
    give_computer_cards()


def game_over():
    """This is just displaying the final messages if the game happens to be over"""
    user_score = add_score(user_cards)
    dealer_score = add_score(dealer_cards)
    print(f"\n\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")


def check_scores():
    """contains the print statements that will dictate whether someone won, tied, or lost"""
    user_score = add_score(user_cards)
    dealer_score = add_score(dealer_cards)
    if user_score > 21:
         print("\n\nYou went over 21! You lose :(")
    elif user_score == 21 and dealer_score == 21:
        print("\n\nYou both hit 21! But it's still a draw :/")
    elif dealer_score == 21:
        print("\n\nAw shucks the dealer just hit 21. You lose :(")
    elif user_score == 21:
        print("\n\nYou just hit 21!!! You should go to a real casino! YOU WIN!")
    elif user_score > dealer_score:
        print("\n\nYour score was higher than the computers score! You win!")
    elif dealer_score > user_score:
        print("\n\nDealer has a higher hand. You lose :(")
    elif user_score == dealer_score:
        print("\n\nYou and the computer had the same score! IT'S A DRAW")

def check_eleven():
    """Ensuring that we can make the 11 a 1 if we are over 21"""
    user_score = add_score(user_cards)
    dealer_score = add_score(dealer_cards)

    if user_score > 21 and user_cards[-1] == 11:
        user_cards[-1] = 1
    elif user_score < 21 and user_cards[-1] == 11:
        user_cards[-1] = 11


    if dealer_score > 21 and dealer_cards[-1] == 11:
        dealer_cards[-1] = 1
    elif dealer_score < 21 and dealer_cards[-1] == 11:
        dealer_cards[-1] = 11


def play_again_question():
    """This is where we can tell the game to play again and go back to the top and clear the lists."""
    decision = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if decision.lower() == 'y':
        return True
    elif decision.lower() == 'n':
        return False
    else: 
        print("I don't know that command. I am going to self destruct!")
        return False

deal_cards()

    
playing = True

while playing:
    check_eleven()
    print(f"Your cards: {user_cards},  current score: {add_score(user_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")


    if add_score(user_cards) >= 21:
        check_eleven()
        check_scores()
        game_over() 
        play_again = play_again_question()
        print(play_again)  
        if play_again == True:
            clear_cards()
            deal_cards()
            cards[0] = 11
            continue
        else:
            playing = False


    hit_decision = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit_decision.lower() == 'y':
        hit_me()
        check_eleven()
        user_score = add_score(user_cards)
        if user_score >= 21:
            check_scores()
            game_over() 
            play_again = play_again_question()
            if play_again == True:
                clear_cards()
                deal_cards()
                cards[0] = 11
                continue
            else:
                playing = False
        else:
            continue
    elif hit_decision.lower() == 'n':
        check_scores()
        game_over()
        play_again = play_again_question()
        if play_again == True:
            clear_cards()
            deal_cards()
            cards[0] = 11
            continue
        else:
            playing = False


