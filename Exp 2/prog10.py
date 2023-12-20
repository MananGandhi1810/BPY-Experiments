# Write a program to generate fibonacci series

n = int(input("Enter a number: "))
a = 0
b = 1
c = 0

for i in range(1, n+1):
    print(a, end=" ")
    c = a + b
    a = b
    b = c