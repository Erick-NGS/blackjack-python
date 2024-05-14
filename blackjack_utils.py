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

def compare(in_user_score, in_computer_score):
    """Checks to see who won the match"""

    if in_user_score > 21 and in_computer_score > 21:
        return "You went over 21. You lose!"
    
    if in_user_score == in_computer_score:
        return "It's a draw!"
    
    elif in_computer_score == 0:
        return "Blackjack! Computer won!"
    
    elif in_user_score == 0:
        return "Blackjack! You won!"
    
    elif in_computer_score > 21:
        return "The computer went over 21, you won!"
    
    elif in_user_score > 21:
        return "You went over 21, the computer won!"
    
    elif in_user_score > in_computer_score:
        return "You win!"
    
    else:
        return "You lose!"