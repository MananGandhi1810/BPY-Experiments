a = [1, 2, 3, 4, 5]
n = int(input("Enter an index: "))

try:
    print(a[n])
    print(a[n]/a[n+1])
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(e)