## po kazdej literze ma byc dash
def f(text):
    result=''
    for char in range(len(text)):
        result += text[char]
        if char < len(text) - 1:
            result += '-'
    return result








print(f(''))
    
