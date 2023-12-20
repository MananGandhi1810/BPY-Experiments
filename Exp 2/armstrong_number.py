num = int(input("Enter a number: "))
sum = 0

for i in str(num):
    sum += int(i)**3

if sum==num:
    print("Armstrong")
else:
    print("Not Armstrong")