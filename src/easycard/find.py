import re
from bankCard import Card

def find_bank_no(content:str):
    card = Card()
    card_no_pat = r"(\d{15,19})"
    card_nos = re.compile(card_no_pat).findall(content)
    cards = []
    for card_no in card_nos:
        card.no = card_no
        if card.verify_len() and card.verify_luhn() and card.verify_card_start():
            cards.append(card_no)
    return cards