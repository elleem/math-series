def fibonacci(n):
    """
    :parm
    :return:
    """
    if n < 0:
        return None
    elif n <= 1:
        return n
    else:
        return  (fibonacci(n-1) + fibonacci(n-2))