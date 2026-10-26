###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    return total


any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')