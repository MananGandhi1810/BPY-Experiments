t = ((1, 2), (2, 3), (4, 2), (2, 4))


def sort(a):
    return a[1]


r = tuple(sorted(list(t), key=sort))
print(r)
