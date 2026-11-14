def f(number1:int,number2:int,operator):
    result = 0
    if operator == '+':
        result = number1 + number2
    elif operator == '%':
        result = number1 % number2
    elif operator == '**':
        result = number1 ** number2
    elif operator == '*':
         result = number1 * number2
    elif operator == '-':
        result = number1 - number2
    return result


print(f(2,3,"**"))