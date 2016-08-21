#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe

import math

# square root
print(math.sqrt(9))

# check if number is integer. useful to check for divisibility
print((9/4).is_integer())

# cast string to int
print(int("3") + 3)

even_nums = [x*2 for x in range(10)]
print(math.fsum(even_nums))

print (math.pow(2,3))