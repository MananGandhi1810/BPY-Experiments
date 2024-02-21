# Write a Python program that calculates sum of square of n integers provided by the user. The program must raise an exception if user enters data of wrong data type.
nums = []
print("Enter n integers (Enter stop to stop): ")
while True:
    try:
        n = input()
        if n.lower() == "stop":
            break
        nums.append(int(n))
    except ValueError:
        print("Please enter an integer")
print("Sum of squares of the integers is: ", sum([i**2 for i in nums]))
