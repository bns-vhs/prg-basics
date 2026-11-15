def f(binary_number:str):
    for char in binary_number:
        if char not in {'1','0'}:
            return False
    return True
        



print(f('1311a10100'))









def suma(amount_to_pay):
    zloty5 = amount_to_pay // 5
    reszta = amount_to_pay % 5
    zloty2 = reszta // 2
    zloty1 = reszta % 2
    return zloty5 + zloty2 + zloty1


print(suma(8))


def liczenie(number,even):
    result=0
    for char in str(number):
        digit= int(char)
        if even and digit % 2 == 0:
            result += digit
        elif not even and digit % 2 !=0:
            result += digit
    return result

print(liczenie(3124,False))



def ujemne(x,y):
    result=0
    for n in range(x,y+1):
        if n % 2 ==0 and n<0:
            result += 1
    return result

print(ujemne(-1,11))


def negatywnosc(n1,n2,n3):
    if n1 <0:
        return True
    elif n2 <0:
        return True
    elif n3 <0:
        return True
    else:
        return False

print(negatywnosc(5,4,14))



def jeden_string(n:int):
    result= ''
    for char in range(1,n+1):
        result+= str(char)
    return result

print(jeden_string(11))

def choinka(n):
    result = ''
    if n ==1:
        result = '*'
    elif n>1:
        result = '*' + (n-1) * '/*'
    return result

print(choinka(4))

def operatory(n1,n2,operator):
    result = 0
    if operator == '+':
        result = n1 + n2
    elif operator == '%':
        result = n1%n2
    elif operator == '**':
        result = n1**n2
    elif operator == '*':
        result = n1*n2
    elif operator == '-':
        result = n1-n2
    return result

print(operatory(1,2,'+'))



def detekcje(detector):
    rezultat = 0
    for znak in detector:
        if znak == '+':
            rezultat +=1
        elif znak == '-':
            rezultat -=1
        
        if rezultat >= 3:
            return True
    return False

print(detekcje("+-+-+-++++-"))




def fibonaczi(n):
    result = 0
    if n == 1:
        result = 0
    elif n == 2:
        result = 1
    elif n>2:
        a = 0
        b = 1
        for liczba in range(3, n+1):
            result = a + b
            a = b
            b = result
    return result

print(fibonaczi(9))


def palindrom(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    return False

print(palindrom('book'))


def usuwanie_spacji(zdanie):
    result = ''
    for char in zdanie:
        if char != ' ':
            result += char
    return result

print(usuwanie_spacji('a a a a a a ebe ebe'))

def ebe(number):
    result =0
    num_str = str(number)
    for char in num_str:
        licznik = 0
        for other_char in num_str:
            if char == other_char:
                licznik += 1
        if licznik >1:
            result += int(char) 
    return result

print(ebe(513553007))


def najmniejsza_najwieksza(n1,n2,n3):
    return max(n1,n2,n3) - min(n1,n2,n3)

print(najmniejsza_najwieksza(7,4,9))