# Write a Python program that prompts the user to input two numbers and raises a ValueError exception if the inputs are not numerical.

a = input("Enter a number: ")
b = input("Enter another number: ")
try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Please enter numerical values")
else:
    print("Correct values entered:", a, b)