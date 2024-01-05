nums = [1, 2, 3, 4, 5]
even = []
odd = []
for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)