#Write a Python program to shuffle the elements of a given list
import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {l}")
random.shuffle(l)
print(f"Shuffled list: {l}")

l = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(f"Original list: {l}")
random.shuffle(l)
print(f"Shuffled list: {l}")