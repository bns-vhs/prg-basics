#### NIE CZAJE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def f(number):
    result= 0
    num_str=str(number)
    for char in num_str:
        count = 0
        for other_char in num_str:
            if char == other_char:
                count +=1
        if count >1:
            result += int(char)
    return result



print(f('1'))







def nwm(numberek):
    result = 0
    str_numberek=str(numberek)
    for char in str_numberek:
        licznik=0
        for inny_char in str_numberek:
            if char == inny_char:
                licznik +=1
        if licznik >1:
                result+=int(char)
    return result


print(nwm(513553007))
