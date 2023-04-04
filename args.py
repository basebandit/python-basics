#!/usr/bin/env python3


def my_sum(my_integers):
    result = 0
    for num in my_integers:
        result += num
    return result


print(my_sum([1]))  # 1
print(my_sum([1, 2]))  # 3


# using *args is much more convenient, especially when you don't upfront how
# many values should go into the list
def sum(*args):
    result = 0
    # print(type(args)) # <class 'tuple'>
    # iterating over args tuple
    for x in args:
        result += x
    return result


print(sum(1, 2, 3))  # 6
print(sum(1))  # 1

# Note that args is just a name. You’re not required to use the name args.
# You can choose any name that you prefer, such as integers:


def sum2(*integers):
    result = 0
    for x in integers:
        result += x
    return result


print(sum2(1))  # 1
print(sum2(3, 4, 5, 7, 8))  # 27

# The above function still works, even if you pass the iterable object as integers
# instead of args. All that matters here is that you use the unpacking operator (*).
