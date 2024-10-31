# waf to print the length of a list
# waf to print the items in a list
# waf to convert dollar into inr
a = [1, 2, 3, 4, 5, 6]
dollar = int(input("write a number: "))

# function one


def val():
    b = len(a)
    print(b)

    # calling
    val()

    # function two


def va1():
    for items in a:
        print(items)

        # calling
        val()

    # function three


def val2():
    n = dollar * 83
    print(n)

    # calling

    val2()
