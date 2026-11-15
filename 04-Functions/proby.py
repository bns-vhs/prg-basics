def card_cryptographic(card_number):
    return card_number[:2] + 10 * '*' + card_number[-4:]

print(card_cryptographic('1011111111110000'))

def payer(amount_to_pay):
    ilosc5= amount_to_pay //5
    reszta= ilosc5 % 5
    ilosc2= reszta //2
    ilosc1= reszta %2
    return ilosc5+ilosc2+ilosc1

print((payer(23)))

def ascii(sentence):
    if len(sentence) %3 == 0:
        return True
    else:
        return False

print(ascii('hello world'))




def hide(card_number):
    return card_number[:2] + 10 * '*' + card_number[-4:]

print(hide('5290312400019022'))