import math
from math import tan, pi
#1
x = 15
print(math.radians(x))

#2
height = 5
a = 5
b = 6
formula_trapezoid = (a + b)/2 * height
print(formula_trapezoid)

#3
n_sides = 4
length_of_side = 25
area_of_polygon = n_sides * (length_of_side ** 2)/(4 * tan(pi/n_sides))
print(area_of_polygon)

#4
height_of_p = 6
length_of_p = 5
area_of_p = height_of_p * length_of_p
print(area_of_p)