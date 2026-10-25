###
# Calculates and prints the total washing time.
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#

total_washing_time = 0

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').lower()
extra_rinse = input('Extra rinse? (y/n): ').lower() == 'y'
extra_spin = input('Extra spin? (y/n): ').lower() == 'y'

# Obliczanie czasu programu głównego
if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20

# Dodawanie czasu dla opcji dodatkowych
if extra_rinse:
    total_washing_time += 15

if extra_spin:
    total_washing_time += 9

print(f"Total washing time: {total_washing_time} minutes")