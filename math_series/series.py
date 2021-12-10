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

# sum_series function
def sum_series(n, first_element = 0, second_element = 1):
    """
    This function takes three parameters and return nth number in the series. If the input is invalid, it would return None.
    
    Parameters:
        - First parameter is required. It determines which element in the series needs to be returned
        - The rest two parameters are optional.
            - Second parameter's default value is 0. It represents the first element in the series.
            - Thrid parameter's default value is 1. It represents the second element in the series.

    How is the series made?
    First two elements in the series are given by the user with arguments. From thrid element, it is the sum of preceding two elements.
    """
    if type(n) is int and n >= 0:
        if n == 0:
            return first_element
        elif n == 1:
             return second_element
        else:
            return sum_series(n - 1, first_element, second_element) + sum_series(n - 2, first_element, second_element)
    else:
        return None