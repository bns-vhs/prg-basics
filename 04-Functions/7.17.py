## 0,1,1,2,3,5,8,13,21,24

def f(n):
    if n == 1:
        value = 0
    elif n == 2:
        value = 1
    else:
        a=0
        b=1
        for i in range(3, n+1):
            value = a + b
            a = b
            b = value
    return value

print(f(9))


def fibonacci(x):
    if x == 1:
        wartosc=0
    elif x == 2:
        wartosc=1
    else:
        z=0
        y=1
        for liczba in range(3, x+1):
            wartosc=z+y
            z=y
            y=wartosc
    return wartosc


print(fibonacci(9))