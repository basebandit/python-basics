#!/usr/bin/env python3

# Basic for loops
#
# for i = 1 to 10
#     <loop body>
#
# Collection-based or iterator-based loop
#
# for i in <collection>
#     <loop body>
#
# Most Python's for loop looks like this:
#
# for <var> in <iterable>:
#     <statement(s)>
#
# <iterable> is a collection of objects—for example, a list or tuple.
# The <statement(s)> in the loop body are denoted by indentation, as
# with all Python control structures, and are executed once for each
# item in <iterable>
a = ["foo", "bar", "baz"]
for i in a:
    print(i)

# If an object is iterable, it can be passed to the built-in Python
# function iter(), which returns something called an iterator.
print(iter("foobar"))  # <str_iterator object at 0x7fd492d1fc70>
print(iter([a]))  # <list_iterator object at 0x7f4bd28ffc70>
# print(iter(42))  # TypeError: 'int' object is not iterable
print(iter({"foo", "bar", "baz"}))  # <set_iterator object at 0x7fab2ed2f9c0>
print(
    iter({"foo": 1, "bar": 2, "baz": 3})
)  # <dict_keyiterator object at 0x7fa401a59440>

# Once you’ve got an iterator, what can you do with it?
# An iterator is essentially a value producer that yields successive values
# from its associated iterable object. The built-in function next() is used
# to obtain the next value from in iterator.
itr1 = iter(a)
itr2 = iter(a)
print(itr1)  # <list_iterator object at 0x7fe2e7267df0>
print(next(itr1))  # foo
print(next(itr1))  # bar
print(next(itr1))  # baz
print(next(itr2))  # foo
# print(next(itr1))  # StopIteration (Note: this error tells you this iterator
# has already reached the end)
#
# Even when iterator itr1 is already at the end of the list, itr2 is still at
# the beginning. Each iterator maintains its own internal state, independent
# of the other.
itr = iter(a)
print(tuple(itr))  # ('foo', 'bar', 'baz')
itr = iter(a)
print(set(itr))  # {'baz', 'bar', 'foo'}

# iterators are "lazy". Items are not created until they are requested. That
# means when you create an iterator, it doesn't generate all the items it can
# yield just then. It waits until you ask for them with next().
#
# a = ["foo", "bar", "baz"]
# for i in a:
#     print(i)
#
# This loop can be described entirely in terms of the concepts you have just
# learned about iterators. To carry out the iteration this for loop describes,
# Python does the following:
#
# 1. Calls iter() to obtain an iterator for a
# 2. Calls next() repeatedly to obtain each item from the iterator in turn
# 3. Terminates the loop when next() raises the StopIteration exception
