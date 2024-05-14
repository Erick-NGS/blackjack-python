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
