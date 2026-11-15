## po kazdej literze ma byc dash
def f(text):
    result=''
    for char in range(len(text)):
        result += text[char]
        if char < len(text) - 1:
            result += '-'
    return result








print(f('eeeeee'))
    





def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n-1)

print(sum_natural(10))





























def trelemorele(text):
    result=''
    for char in range(len(text)):
        result += text[char]
        if char <len(text) -1:
            result += '-'
    return result


print(trelemorele('eloelo'))
            
