# Write a function division() that accepts two arguments. The function should be able to catch an exception such as ZeroDivisionError, ValueError, or any unknown error you might come across when you are doing a division operation.
def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Wrong values for division")
    except:
        print("An unknown error occured")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
res = division(a, b)
if res:
    print("Result of division is: ", res)