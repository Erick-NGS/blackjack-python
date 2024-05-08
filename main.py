from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_card():
    """Deal a random card to an user"""
    selected_card = random.choice(cards)
    return selected_card

# User cards
user_cards.append(deal_card())
user_cards.append(deal_card())

# Computer cards
computer_cards.append(deal_card())
computer_cards.append(deal_card())

