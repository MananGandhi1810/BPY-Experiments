sample = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
res = sample[-1]

for i in sample:
    if sum(res)>sum(i):
        res = i

print(res)