age = int(input('How old are you?'))
group = 'none'

if age<13:
    group = 'child'
elif age in range(13,21):
    group = 'teen'
elif age in range(20,64):
    group = 'adult'
elif age>65:
    group = 'senior'
else:
    print("You don't exist.")
print(f'You belong to the {group} group')
