"""
Accept the marks for the number of subjects studying in this semester. While accepting marks check the constraints that entered marks should not be negative as well as should not be more than 100 (if entered terminate the code). If the constraint is satisfied, calculate the total & percentage. If % is greater than equal to 92 display “Merit” if % is between 75 and 91 display “Distinction” if % is between 60 and 74 “First class” if % is between 45 to 59 display “Second class” else display “Fail”.
"""

subjects = int(input("Enter the number of subjects: "))
total = 0

for i in range(1, subjects + 1):
    marks = int(input(f"Enter the marks for subject {i}: "))
    if marks < 0 or marks > 100:
        print("Invalid marks entered")
        exit()
    total += marks

percentage = total / (subjects * 100)

if percentage >= 0.92:
    print("Merit")
elif percentage >= 0.75:
    print("Distinction")
elif percentage >= 0.60:
    print("First class")
elif percentage >= 0.45:
    print("Second class")
else:
    print("Fail")