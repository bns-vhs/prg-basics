def month(n):
    name = ''
    if n == 1:
        name = 'January'
    elif n == 2:
        name = 'February'
    elif n == 3:
        name = 'March'
    elif n == 4:
        name = 'April'
    elif n == 5:
        name = 'May'
    elif n == 6:
        name = 'June'
    elif n == 7:
        name = 'July'
    elif n == 8:
        name = 'August'
    elif n == 9:
        name = 'September'
    elif n == 10:
        name = 'October'
    elif n == 11:
        name = 'November'
    elif n == 12:
        name = 'December'
    else:
        name = 'Invalid month number'
    return name


n = int(input('Enter month number: '))
print('The name of month', n, 'is', month(n))
