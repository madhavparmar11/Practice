# sum of n numbers with recursion


def show(n):
    if n == 0 or n == 1:
        return
    d = show(n)
    show(n - 1)
    for items in d:
        return items + d(items + 1)

        # calling

    r = show(6)
    print(r)
