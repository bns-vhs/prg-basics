def f(amount_to_pay):
    coins5 = amount_to_pay // 5
    reszta = amount_to_pay % 5
    coins2 = reszta //2
    coins1 = reszta %2
    return coins5 + coins2 + coins1 and f"ilosc 5 ={coins5}, ilosc 2={coins2}, ilosc1={coins1}"

print(f(203))

def ile_pieniazkow_jestes_winny(ile_musisz_zaplacic):
    pieciozlotowek= ile_musisz_zaplacic //5
    resztka= ile_musisz_zaplacic % 5
    dwuzlotowek= resztka //2
    zlotowek= resztka % 2
    return pieciozlotowek + dwuzlotowek + zlotowek

print(ile_pieniazkow_jestes_winny(23))