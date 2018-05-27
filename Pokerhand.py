import re
def check_card(cards):
    cards_value=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for c in cards:
        if c not in cards_value:
            return 0
        else:
            pass
    return 1
def check_suit(suits):
    suit_value=['H','C','D','S']
    for c in suits:
        if c not in suit_value:
            return 0
        else:
            pass
    return 1
def check_string(check_value):
    suit_value=['H','C','D','S']
    check=bool(re.search('\s',check_value))
    if check == True: 
        return 3
    else:
        if check_value[0] not in suit_value:
            return 1
        else: return 0
def desk(hand):
    checks_string=check_string(hand)# Check Input String Format
    cards = []
    suits = []
    list_covert=list(hand)
    if checks_string == 3:
        return "Error Format String!!!"
    else:
        if checks_string==1:
            for l in list_covert:
                index = list_covert.index(l)
                if index % 2 == 0:
                    cards.append(l)
                else: suits.append(l)
        else:
            for l in list_covert:
                index = list_covert.index(l)
                if index % 2 == 0:
                    suits.append(l)
                else: cards.append(l)
        check_cards=check_card(cards)# Check Card
        check_suits=check_suit(suits)# Check Suit
        if check_cards == 1 and check_suits == 1: 
            same_cards = sorted([cards.count(a) for a in set(cards)])
            if len(same_cards) == 2:
                if max(same_cards) == 4: # Four Cards
                    return "4C"
                elif max(same_cards) == 3: # Full House
                    return "FH"
            elif len(same_cards) == 3:
                if max(same_cards) == 3: # Three Cards
                    return "3C"
                else: # Two pair
                    return "2P"
            elif len(same_cards) == 4:# One Pair
                return "1P"
            else: # No hands
                return "-------"
        else: return "Error card or suit...."       

if __name__ == "__main__":
    hand=input('input string poker hand: ')
    print (desk(hand))
