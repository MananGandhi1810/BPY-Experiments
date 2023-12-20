# Write a Python program to Read a Number n and Print the Sum of odd Natural Numbers between the range of 1 to n both inclusive
n = int(input("Enter a number: "))
sum = 0
i = 1

while i<=n:
    sum+=i
    i+=1

print(f"Sum of first {n} natural numbers is {sum}")