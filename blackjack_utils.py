import random

def deal_card():
    """Deal a random card to an user"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(cards)
    return selected_card

def calculate_score(list_cards):
    """Calculates the score of the user"""
    total_score = sum(list_cards)
    if total_score == 21 and len(list_cards) == 2:
        return 0
    
    if 11 in list_cards and total_score > 21:
        list_cards.remove(11)
        list_cards.append(1)

    return total_score