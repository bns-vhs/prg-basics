def f(expression):
    result=0
    sign='+'
    for i in expression:
        if i == '+':
            sign ='+'
        elif i== '-':
            sign ='-'
        else:
            if sign == '+':
                result += int(i)
            elif sign == '-':
                result -= int(i)
    return result


print(f('1-1+1'))