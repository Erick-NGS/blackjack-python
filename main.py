from art import logo
import blackjack_utils

user_cards = []
computer_cards = []
is_game_over = False

# User cards
user_cards.append(blackjack_utils.deal_card())
user_cards.append(blackjack_utils.deal_card())

# Computer cards
computer_cards.append(blackjack_utils.deal_card())
computer_cards.append(blackjack_utils.deal_card())

user_score = blackjack_utils.calculate_score(user_cards)
computer_score = blackjack_utils.calculate_score(computer_cards)
# print(f"User cards = {user_cards} / User score = {user_score}")
# print(f"Computer 1st cards = {computer_cards[0]}")

while not is_game_over:
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True

    else:
        deal_card_question = input("Do you want to draw another card?('Y' for yes, 'N' for no): ")
        if deal_card_question.lower() == "y":
            user_cards.append(blackjack_utils.deal_card())
            print(f"User cards: {user_cards}")

        else:
            is_game_over = True


while computer_score != 0 and computer_score < 17:
    computer_cards.append(blackjack_utils.deal_card())
    computer_score = blackjack_utils.calculate_score(computer_cards)