def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(13))


def lucas(n):
    a = 2
    b = 1

    if (n == 0):
        return a

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


print(lucas(29))


def sum_series(n, first_number=0, second_number=1):
    if n == 1:
        return first_number
    elif n == 2:
        return second_number
    else:
        return sum_series(n - 2, first_number, second_number) + sum_series(n - 1, first_number, second_number)
