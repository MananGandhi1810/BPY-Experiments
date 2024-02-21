# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

import random


l = range(random.randint(1, 10))
n = int(input("Enter an index: "))

try:
    print(l[n])
except IndexError:
    print("Index out of range")