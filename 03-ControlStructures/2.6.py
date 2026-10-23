number = int(input('Enter your number:'))
if number >0:
    print(f'{number} is positive')
elif number ==0:
    print(f'{number} is zero')
elif number <0:
    print(f'{number} is negative')
else:
    print('I dont know what you did to get this message...')