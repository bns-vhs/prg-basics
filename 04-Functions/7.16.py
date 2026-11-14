def f(sentence):
    result=""
    for char in sentence:
        if char != " ":
            result += char
    return result



print(f("integrated development environment"))



def zdanko(zdanie):
    wynik=''
    for literka in zdanie:
        if literka != ' ':
            wynik += literka
    return wynik



print(zdanko('dzikie weze'))