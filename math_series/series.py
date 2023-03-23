def fibonacci(n):
    """
    Calculate n of the Fibonacci sequence.
    :parm n of the index to calculate
    :return: the n of the index in the Fibonacci sequence
    """
    if n < 0:
        return None
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Calculate n of the Lucas sequence.
     :parm n of the index to calculate
    :return: the n of the index in the Lucas sequence.
    """
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, first=0, second=1):
    """
    :parm
    :return:
    """
    if first== 0 and second==1:
       return fibonacci(n)
    elif first == 2 and second ==1:
       return lucas(n)