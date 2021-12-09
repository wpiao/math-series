# fibonacci function
def fibonacci(n):
    """
    This function takes input n and return nth number in fibonacci series.
    If input is invalid - such as negative number, string, float, etc., it would return None
    """
    if type(n) is int and n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return None

# lucas function
def lucas(n):
    """
    This function takes input n and return nth number in Lucas series.
    If input is invalid - such as negative number, float, string, etc., it would return None
    """
    if type(n) is int and n >= 0:
        if n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            return lucas(n - 1) + lucas(n - 2)
    else:
        return None