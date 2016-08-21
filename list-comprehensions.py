#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe

from math import sqrt

# create a list of even numbers

even_nums = [x*2 for x in range(10)]
print(even_nums)

perfect_sqrs = [x for x in range(10) if sqrt(x).is_integer()]
print(perfect_sqrs)

unperfect_sqrs = [x for x in range(10) if x not in perfect_sqrs]
print(unperfect_sqrs)

tuples = [(x, y) for x in range(4) for y in range(3)]
# probably useful for things like co-ordinates
print(tuples)
