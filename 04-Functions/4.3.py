###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
import math
def triangle_area(a,b,c):
    obwod = (a+b+c)/2
    heron= math.sqrt(obwod*(obwod-a)*(obwod-b)*(obwod-c))
    return heron

a = 3
b = 4
c = 5

print(f'The area of ​​a triangle with sides {a} {b} {c} is {triangle_area}')
print(f'The area of ​​a triangle with sides {a} {b} {c} is ...')
print(f'The area of ​​a triangle with sides {a} {b} {c} is ...')