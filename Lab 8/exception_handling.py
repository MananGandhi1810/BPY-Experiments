a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    c = a/b
    print(c)
except Exception as e:
    print(e)
    print("Error dividing numbers")