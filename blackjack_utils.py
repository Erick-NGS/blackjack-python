import random

def deal_card():
    """Deal a random card to an user"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(cards)
    return selected_card

def calculate_score(list_cards):
    """Calculates the score of the user"""
    total_score = sum(list_cards)
    return total_score