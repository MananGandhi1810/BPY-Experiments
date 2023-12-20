"""
Write a Python program to accept percentage from the user and display the grade according to following criteria:
Percentage > 90% : Grade A
Percentage > 80% and <= 90% : Grade B
Percentage > 60% and <= 80%: Grade C
Below 60%: Grade D
"""

percentage = float(input("Enter your percentage: "))
if percentage > 90:
    print("Grade A")
elif percentage > 80:
    print("Grade B")
elif percentage > 60:
    print("Grade C")
else:
    print("Grade D")