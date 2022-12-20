def fibonacci(n):
    """the code for fib seq where (n-2) + (n-1) = n"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """the code for lucas seq where (n-2) + (n-1) = n"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, m=0, o=1):
    """the code for either seq where (n-2) + (n-1) = n"""
    if n == 0:
        return m
    if n == 1:
        return o
    else:
        return sum_series(n - 2, m, o) + sum_series(n - 1, m, o)


print("hi")