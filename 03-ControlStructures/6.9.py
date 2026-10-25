name = input("What's your FEMALE name?")

if name and name[-1] == 'a' or 'A':
    print(name)
else:
    print(f'{name} is NOT, a female name!')