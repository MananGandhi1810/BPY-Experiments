def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(result)
    finally:
        print("Division done")

divide(1, 0)
divide(1, 2)