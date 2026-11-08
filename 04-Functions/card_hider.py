def hide(card_number:str) ->str:
    return card_number[:2] + '*'*10 + card_number[-4:]