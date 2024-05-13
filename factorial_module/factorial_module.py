def factorial_iterative(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def clumsy(n):
    if n <= 2:
        return n
    elif n <= 4:
        return n + 3
    elif n % 4 == 0:
        return n + 1
    elif n % 4 <= 2:
        return n + 2
    else:
        return n - 1