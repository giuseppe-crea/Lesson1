# interfaces and stuff

def sum(m, n):
    # iterator_val = 0
    if not isinstance(n, int) or not isinstance(m, int):
        raise ValueError('Not an int')
    if n >= 0:
        iterator_val = 1
    else:
        iterator_val = -1
    for i in range(abs(n)):
        m += iterator_val
    return m


def divide(m, n):
    i = 0
    sign = 1
    if n == 0:
        raise ValueError('Division by Zero.')
    if not isinstance(n, int) or not isinstance(m, int):
        raise ValueError('Not an int')
    if n < 0:
        sign = -1
    if m < 0:
        sign = -sign
        m = -m
    while m > 0:
        m -= abs(n)
        i += 1
    return i*sign
