t = ("a", "p", "p", "l", "e")
print(t.count("p"))
print(t.index("l"))
for i in t:
    print(i)
# t[0] = 1 # This is an error because tuples are immutable
print("a" in t)
print("b" in t)
l = list(t)
l.append("s")
t = tuple(l)
print(t)
