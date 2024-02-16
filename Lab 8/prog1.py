def division(a, b):
    try:
        c = a/b
        print(c)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)
    
division(1, 0)
division(1, "a")
division(1, 2)