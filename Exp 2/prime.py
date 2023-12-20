num = int(input("Enter a number: "))
found = False

for i in range(1, (num//2)+1):
    if num%i==0:
        print("Not Prime")
        found = True
        break

if not found:
    print("Prime")