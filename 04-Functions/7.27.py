def f(product_code):
    suma = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    if int(product_code[3]) == suma % 7:
            result=True
    else:
        result=False
    return result



print(f('1082'))