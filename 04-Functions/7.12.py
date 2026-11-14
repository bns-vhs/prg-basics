def f(n):
    result=""
    if n==1:
        result = '*'
    elif n>1:
        result = '*' + (n-1) * '/*'
    return result


print(f(1))