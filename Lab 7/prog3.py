import random

nums = list(range(2))
original = nums[::-1]
count = 0
while nums != original:
    random.shuffle(nums)
    count += 1

print(count)