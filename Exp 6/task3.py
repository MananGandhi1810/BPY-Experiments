from calc import addition, subtraction

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f"The sum of {a} and {b} is: {addition(a, b)}")
print(f"The difference of {a} and {b} is: {subtraction(a, b)}")