def f(number,even):
    total=0
    for char in str(number):
        digit= int(char)
        if even and digit % 2 == 0:
            total += digit
        elif not even and digit % 2 != 0:
            total += digit
    return(total)



print(f(13115,True))



def f(cyferka, parzysta):
    totalnie = 0
    for charo in str(cyferka):
        cwelerka= int(charo)
        if parzysta and cwelerka % 2 == 0:
            totalnie += cwelerka
        elif not parzysta and cwelerka % 2 != 0:
            totalnie += cwelerka
    return(totalnie)


print(f(12345,True))