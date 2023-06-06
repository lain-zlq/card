from bankCard import Card

def bank_no_verify(bank_no:str):
    card = Card(bank_no)
    return card.verify_len() and card.verify_luhn() and card.verify_card_start()
