light_switch1 = bool(int(input('Is first light switch on? (1/0): ')))
light_switch2 = bool(int(input('Is second light switch on? (1/0): ')))
on = "are"
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
if bulbs_on == 1:
    on = "is"

print(f'currently there {on} {bulbs_on} lightbulbs on')