def f(name):
    acronym=""
    for char in range(len(name)):
        if name[char] != " " and (char==0 or name[char - 1] == ' '):
            acronym += name[char]
    return acronym



print(f('Internet of Things'))



























def f_akronym(nazwa):
    akronym=''
    for literka in range(len(nazwa)):
        if nazwa[literka] != ' ' and (literka == 0 or nazwa[literka - 1] == ' '):
            akronym += nazwa[literka]
    return akronym


print(f_akronym('Internet of Things'))