def f(x,y):
    rang = 0
    for char in range(x,y+1):
        if char < 0 and char %2 == 0:
            rang += 1
    return rang



print(f(-7,8))


def liczydlo(a,b):
    rezultat=0
    for literka in range(a,b+1):
        if literka < 0 and not literka %2 != 0:
            rezultat += 1
    return rezultat

print(liczydlo(-1,11))