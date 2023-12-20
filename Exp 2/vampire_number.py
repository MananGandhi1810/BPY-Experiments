num = int(input("Enter a number: "))
factors = []

for i in range(1, (num//2)+1):
    if num%i==0:
        factors.append(i)

for i in factors:
    for j in factors:
        if i*j==num and sorted(list(str(num))) == sorted(list(str(i)+str(j))) and len(str(i))==len(str(j)):
            print(i, j)