###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume= a*b*c
area= 2*(a*b+b*c+c*a)
print (f"volume is {volume} and surface is {area}")