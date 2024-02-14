# Write a Python program to calculate area of a circle (Pi*r*r). Take value of radius from the user. Use in-build math module for the value of pi.
from math import pi

r = float(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {r} is: {pi * r ** 2}")