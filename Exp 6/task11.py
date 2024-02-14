from calculator import factorial, fibonacci

n = int(input("Enter a number: "))

print(f"The factorial of {n} is: {factorial(n)}")
print(f"The fibonacci series of {n} is:")
res = fibonacci(n)
for i in range(n):
    print(i, end = " ")
print()