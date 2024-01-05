start = int(input("Enter start: "))
end = int(input("Enter end: "))
even = []
for i in range(start, end+1):
    if i%2==0:
        even.append(i)
print(even)