def inrange(x:int,y:int,n:int) ->int:
    if x<=n<=y:
        result=True
    elif y<=n<=x:
        result=True
    else:
        result=False
    return(result)

def counter(text:str,letter:str) ->int:
    result = 0
    for char in text:
        if char == letter:
            result += 1
    return(result)


x=15
y=2
n=13

print(inrange(x,y,n))
print(counter('aaaaaaaaaaaaaeeeeeeeeeaeeeeaeeeeeae','e'))
































def counting_letters(litera:str,slowo:str) ->int:
    result=0
    for char in slowo:
        if char == litera:
            result+=1
    return(result)

print(counting_letters('e','eeeeeBBBB'))

def w_zasiegu(zmienna:int,pierwsza:int,druga:int):
    if pierwsza<=zmienna<=druga:
        rezultat=True
    elif druga<=zmienna<=pierwsza:
        rezultat=True
    else:
        rezultat=False
    return(rezultat)


print(w_zasiegu(3,15,2))