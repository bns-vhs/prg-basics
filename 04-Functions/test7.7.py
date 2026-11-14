def f(binary_number:str)->bool:
    for char in binary_number:
        if char !='1' and char !='0':
            return False
    return True


print(f('11110000'))

































def f(numer_binarny:str)->bool:
    for cyferka in numer_binarny:
        if cyferka !='1' and cyferka !='0':
            return False
    return True

print(f('11110'))