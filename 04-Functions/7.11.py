def f(n1:float,n2:float,n3:float):
    if n1 < 0:
        result=True
    elif n2 < 0:
        result=True
    elif n3 < 0:
        result=True
    else:
        result=False
    return result

print(f(1,2,3))