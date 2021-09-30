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


print("10 + 8: " + str(sum(10, 8)))
try:
    print("10 + 8.1: " + str(sum(10, 8.1)))
except ValueError as e:
    print("10 + 8.1: " + str(e))
print("10 + -8: " + str(sum(10, -8)))
print("10 + 0: " + str(sum(10, 0)))
print("12 / 3: " + str(divide(12, 3)))
try:
    print("12 / 3.1: " + str(divide(12, 3.1)))
except ValueError as e:
    print("12 / 3.1: " + str(e))
print("12 / -3: " + str(divide(12, -3)))
print("-12 / -3: " + str(divide(-12, -3)))
print("-12 / 3: " + str(divide(12, 3)))
try:
    print("12 / 0: " + str(divide(12, 0)))
except ValueError as e:
    print("12 / 0 : " + str(e))
