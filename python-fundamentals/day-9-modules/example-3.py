# Import a specific function from a module

from random import randrange
from math import fsum, remainder, sqrt
# multiple functions can be imported from module. Thi is achieved by separating functions by a comma ','
# Example:
from os import times, system

rand_num = randrange(1, 100)
print('Random number between 1 and 100 is: %d' % rand_num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(pow(2, 8))
print(remainder(30, 12))
print(sqrt(40))