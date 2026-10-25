dog_age = float(0)
human_age = int(input("What's your age?"))
if human_age<=2:
    dog_age= 10.5*(human_age)
elif human_age>2:
    dog_age= 21+(((human_age)-2)*4)
print(f'Your age is {human_age} and your dog age is {dog_age}')



