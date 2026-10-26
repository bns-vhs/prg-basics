###
# Functions to read any data type from the keyboard
#
def input_string(message):
    string = input(message)
    return string

def input_integer(message):
    integer = input(message)
    return int(integer)

def input_real(message):
    real = input(message)
    return float(real)

def input_boolean(message):
    boolean = input(message)
    return bool(boolean)

if __name__ == '__main__':

    integer_number = input_integer('Enter an integer number: ')
    print(f'You entered the integer number {integer_number}')
    string_value = input_string('Enter a string: ')
    print(f'You entered the string "{string_value}"')
    real_value = input_real('Enter a real number: ')
    print(f'You entered the real number {real_value}')
    boolean_value = input_boolean('Enter a boolean value: ')
    print(f'You entered the boolean value {boolean_value}')