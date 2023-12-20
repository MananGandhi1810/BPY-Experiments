# Write a program to reverse a number

num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print(f"Reverse of {original} is {rev}")