#!/usr/bin/env python3


# **kwargs works just like *args, but instead of accepting positional arguments
# it accepts keyword (or named) arguments.
import re


def concatenate(**kwargs):
    result = ""
    # print(type(kwargs)) # <class 'dict'>
    # iterating over the python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result


print(concatenate(a="Python", b="Is", c="Great", d="!"))  # PythonIsGreat!


# kwargs is also just a name that can be changed to whatever you want. Again,
# what is important here is the use of the unpacking operator (**).
def concat(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result


print(concat(a="Python", b=" ", c="Is", d=" ", e="Great", f="!"))  # Python Is Great!

# the example above the iterable object is a standard dict. If you iterate over
# the dictionary and want to return its values, like in the example shown, then
# you must use .values().
# if you forget to use this method, you will find yourself iterating through
# the keys of your Python kwargs dictionary instead, like below


def concatKeys(**kwargs):
    result = ""
    for arg in kwargs:
        result += arg
    return result


print(concatKeys(a="Python", b="Is", c="A", d="Great", e="Language"))  # abcde

# Note: The single asterisk operator * can be used on any iterable that
# Python provides, while the double asterisk operator ** can only be used on
# dictionaries.
my_list = [1, 2, 3]
print(my_list)  # [1, 2, 3]

# below we unpack the list first then print individual values.
print(*my_list)  # 1 2 3


# Note if your function requires a specific number of arguments, you can still use the
# unpacking approach but the iterable you unpack must have the same numer of elements as
# the function arguments.
# See below example:
def another_sum(a, b, c):
    print(a + b + c)


my_list = [1, 2, 3]
another_sum(*my_list)  # 6
# The 3 elements in my_list match up perfectly with the required arguments in another_sum().


# see what happens if you call the function with the wrong number of elements as the function
# arguments
def wrong_sum(a, b, c):
    print(a + b + c)


my_list = [1, 2, 3, 4]
# wrong_sum(
#     *my_list
# )  # TypeError: wrong_sum() takes 3 positional arguments but 4 were given


# When you use the * operator to unpack a list and pass arguments to a function,
# it’s exactly as though you’re passing every single argument alone. This means
# that you can use multiple unpacking operators to get values from several
# lists and pass them all to a single function.
def _sum(*args):
    result = 0
    for x in args:
        result += x
    return result


list_1 = [1, 2, 3]
list_2 = [4, 5]
list_3 = [6, 7, 8, 9]
print(_sum(*list_1, *list_2, *list_3))  # 45

# Say you want to split the list into three different parts i.e the 1st value, last
# value and all the values in between. You can use the unpack operator for this.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, *b, c = my_list
print(a)  # 1
print(b)  # [2, 3, 4, 5, 6, 7, 8]
print(c)  # 9

# How about merging lists use *args
first_list = [1, 2, 3]
second_list = [4, 5, 6]
merged_list = [*first_list, *second_list]

print(merged_list)  # [1, 2, 3, 4, 5, 6]

# Merging two dictionaries, use **kwargs
first_dict = {"A": 1, "B": 2}
second_dict = {"C": 3, "D": 4}
merged_dict = {**first_dict, **second_dict}
print(merged_dict)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# Remember * operator works on any iterable object. It can also be used to
# unpack a string:
a = [*"Real Python"]
print(a)  # ['R', 'e', 'a', 'l', ' ', 'P', 'y', 't', 'h', 'o', 'n']

# The above example above could also be written like below. However this is
# not readable. It is not immediately obvious what it does.
(*a,) = "RealPython"
print(a)  # ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']
# The above expression just takes the string RealPython and assigns all the
# items to the new list a, thanks to the unpacking operator *
# The comma after the a does the trick. When you use the unpacking operator
# with variable assignment, Python requires that your resulting variable is
# either a list or a tuple. With the trailing comma, you have defined a tuple
# with only one named variable, a, which is the list ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n'].

*a, b = "RealPython"
print(b)  # n
print(a)  # ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o']
print(type(b))  # <class 'str'>
print(type(a))  # <class 'list'>

# While the above techniques of unpacking are a neat trick, many Pythonistas
# would not consider this code to be very readable. As such, it’s best to use
# these kinds of constructions sparingly.


# Note: when using *args and **kwargs together with other positional arguments,
# order matters. The *args comes before the **kwargs but after the last
# positional argument
def my_function(a, b, *args, **kwargs):
    pass


# What happens if you change the order? Invalid syntax
# def wrong_function(a,b,**kwargs,*args):
#   pass
# In this case, since *args comes after **kwargs, the Python interpreter
# throws a SyntaxError: invalid syntax
