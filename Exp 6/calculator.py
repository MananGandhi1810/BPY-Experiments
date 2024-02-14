def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)