##Write a program that calculates how many times the given letter appears in any text. Then create a program and check
##how many times the letter 'e' appears in the text below.
##In a separate module, define a function for making calculations.

from count_letters import count_letters
from within_range import within_range
sample_text = "e aaaa eEeE"

target_letter = "e"
occurrences = count_letters(sample_text, target_letter)
x=6
y=12
in_range = within_range(occurrences,x,y)
result= 'yes' if in_range else 'no'
print(f"Litera '{target_letter}' występuje w podanym tekście {occurrences} razy.")
print(f'In range <6,12>? {result}')