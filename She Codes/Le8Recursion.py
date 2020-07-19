def sum(x):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

  # sum(1)
    1
 #sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    "*** YOUR CODE HERE ***"
    if x == 0:
        return 0
    else:
        return sum(x-1) + x


print(sum(6))

def sum_every_other_number(n):
    """Return the sum of every other natural number
    up to n, inclusive.

# sum_every_other_number(8)
    20= 8+6+4+2
#sum_every_other_number(9)
    25 = 9+7+5+3+1
    6+4+2
    """
    if n <= 0:
        return 0
    else:
        return n + sum_every_other_number(n - 2)

print(sum_every_other_number(9))

def fibonacci(n):
    """Return the nth fibonacci number.

# fibonacci(11) = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
    89
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(11))
#
# def paths(m, n):
#     # """Return the number of paths from one corner of an
#     # M by N grid to the opposite corner.
#     #
#     # >>> paths(2, 2)
#     # 2
#     # >>> paths(5, 7)
#     # 210
#     # >>> paths(117, 1)
#     # 1
#     # >>> paths(1, 157)
#     # 1
#     # """
#     # "*** YOUR CODE HERE ***"
#     if m <= 1 or n <= 1:
#         return 1
#     else:
#         return paths((n-1),(m -1)) + (m-1) + (n-1)



def paths(x, y):
    if x == 1 and y == 1:
        return 1

    ret = 0

    if x > 1:
        ret += paths(x-1, y)

    if y > 1:
        ret += paths(x, y-1)

    return ret
print(paths(7, 5))