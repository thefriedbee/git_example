def sum(x, y):
    """Returns the sum of x and y."""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def power(x, y):
    """Returns x raised to the power of y."""
    return x ** y

def divide(x, y):
    """Returns the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def factor(n):
    """Returns the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

