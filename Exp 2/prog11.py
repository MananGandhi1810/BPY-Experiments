# Write a program to print all the strong numbers between 1 to 100

for i in range(101):
    sum = 0
    temp = i
    while temp > 0:
        fact = 1
        digit = temp % 10
        for j in range(1, digit+1):
            fact *= j
        sum += fact
        temp //= 10
    if sum == i:
        print(i)