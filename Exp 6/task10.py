# Write a Python program to print calendar for a particular year using inbuilt calendar module.

from calendar import calendar

year = int(input("Enter the year: "))

print(calendar(year))