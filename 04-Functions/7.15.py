def f(detector):
    people=0
    for sign in detector:
        if sign =='+':
            people+=1
        elif sign =='-':
            people-=1

        if people >=3:
            return True
    return False


print(f('+-+-+-+-'))























def czunik(czujnik):
    ludzie = 0
    for znak in czujnik:
        if znak =='+':
            ludzie +=1
        elif znak =='-':
            ludzie -=1

        if ludzie >=3:
            return True
    return False


print(czunik('+-+++-+---'))