# Write a Python program to print current year, month and today’s date using in-built datetime module.

from datetime import date

print(f"Today's date is: {date.today()}")
print(f"Year: {date.today().year}")
print(f"Month: {date.today().month}")