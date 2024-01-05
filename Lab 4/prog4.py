nums = [1, 2, 3, 4, 5]
small = nums[0]
large = nums[0]
for i in nums:
    if i < small:
        small = i
    if i > large:
        large = i
print(small)
print(large)
