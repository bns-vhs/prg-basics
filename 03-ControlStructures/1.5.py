###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = int(input('Enter you salary'))
total_salary = int(0)
bonus = float(input('enter your bonus')) # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y',

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    ...

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')