from art import logo
import blackjack_utils
import os

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # User cards
    user_cards.append(blackjack_utils.deal_card())
    user_cards.append(blackjack_utils.deal_card())

    # Computer cards
    computer_cards.append(blackjack_utils.deal_card())
    computer_cards.append(blackjack_utils.deal_card())

    print(f"{logo}\n")

    while not is_game_over:
        user_score = blackjack_utils.calculate_score(user_cards)
        computer_score = blackjack_utils.calculate_score(computer_cards)
        # print(f"User cards = {user_cards} / User score = {user_score}")
        # print(f"Computer 1st cards = {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            deal_card_question = input("Do you want to draw another card?('Y' for yes, 'N' for no): ")
            if deal_card_question.lower() == "y":
                user_cards.append(blackjack_utils.deal_card())
                print(f"User cards: {user_cards} = {sum(user_cards)}")

            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(blackjack_utils.deal_card())
        computer_score = blackjack_utils.calculate_score(computer_cards)

    
    os.system('cls||clear')
    print(f"{logo}\n")
    print(blackjack_utils.compare(user_score, computer_score))
    print(f"Your final hand is {user_cards} / Your score was {user_score}!")
    print(f"Your opponent final hand is {computer_cards} / Your opponent score was {computer_score}!\n")


while input("Do you want to play a game of Blackjack?('y' for yes, 'n' for no): ") == "y":
    os.system('cls||clear')
    play_game()
    