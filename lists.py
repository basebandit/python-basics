#!/usr/bin/env python3

import copy
import random

# ===================== TUPLES ======================= #

# Tuples are immutable sequences (ordered list of values)
# Tuples are ordered with finite lenth.
# Tuples can contain values of different types.

my_first_tuple = (1, 2, 3)
print(type(my_first_tuple))  # <class 'tuple'>
print(my_first_tuple)

another_tuple = (1, 2, "three")
print(another_tuple)

empty_tuple = ()
print(empty_tuple)

"""
x = (1)
print(type(x))   <class 'int'>
When you surround a value with parentheses, but don’t include any
commas, Python interprets the value not as a tuple but as the type of
value inside the parentheses. So, in this case, (1) is a just a weird way
of writing the integer 1.
"""
x = (1,)
print(type(x))  # <class 'tuple'>

# build a tuple from another sequence type (string)
a_tuple = tuple("Python")
print(a_tuple)  # ('P', 'y', 't', 'h', 'o', 'n')

numbers = (1, 2, 3)
print(len(numbers))

name = tuple("David")
print(name[2])  # v
print(name[2:4])  # ('v', 'i')

values = (1, 2, 5, 7, 9)
print(values[2])  # 5
print(values[2:4])  # (5, 7)

# Tuples are iterable
vowels = ("a", "e", "i", "o", "u")
for vowel in vowels:
    print(vowel.upper())

# Tuple packing and unpacking
coordinates = 4.21, 9.29  # values are packed into one variable
print(type(coordinates))  # <class 'tuple'>

x, y = coordinates  # values unpacked into two distinct variables
print(x)  # 4.21
print(y)  # 9.29

name, age, occupation = "David", 34, "programmer"
print(name)
print(age)
print(occupation)

# checking existence of values with in
vowels = ("a", "e", "i", "o", "u")
print("o" in vowels)  # True
print("x" in vowels)  # False


# returning multiple values from a function
def adder_subtractor(num1, num2):
    return (num1 + num2, num1 - num2)


print(adder_subtractor(3, 2))  # (5, 1)

# ============= Review Exercises =====================
# 1. Create a tuple literal named cardinal_numbers that holds the strings
# "first", "second" and "third", in that order.
cardinal_numbers = ("first", "second", "third")
print(cardinal_numbers)

# 2. Using index notation and print(), display the string at index 1 in
# cardinal_numbers.
print(cardinal_numbers[1])  # second

# 3. Unpack the values in cardinal_numbers into three new strings
# named position1, position2 and position3 in a single line of code,
# then print each value on a separate line.
position1, position2, position3 = cardinal_numbers
print(position1)
print(position2)
print(position3)

# 4. Create a tuple called my_name that contains the letters of your name
# by using tuple() and a string literal.
my_name = tuple("evanson")
print(my_name)  # ('e', 'v', 'a', 'n', 's', 'o', 'n')
# my_name[2] = "b" tuples are immutable
# print(my_name) # TypeError: 'tuple' object does not support item assignment

# 5. Check whether or not the character "x" is in my_name using the in
# keyword.
print("x" in my_name)  # False


# 6. Create a new tuple containing all but the ﬁrst letter in my_name using
# slicing notation.
new_name = my_name[1:]
print(new_name)  # ('v', 'a', 'n', 's', 'o', 'n')

# =============== End of Review Exercise ================


# ================== Lists ===========================
# Lists are mutable

# list literal
colors = ["red", "yellow", "green", "blue"]
print(type(colors))  # <class 'list'>
print(colors)  # ['red', 'yellow', 'green', 'blue']
# create list from tuple (1,2,3)
numbers = list((1, 2, 3))
print(numbers)  # [1, 2, 3]

# create list from string literal
print(list("python"))  # ['p', 'y', 't', 'h', 'o', 'n']

groceries = "eggs, milk, cheese"
grocery_list = groceries.split(", ")
print(grocery_list)  # ['eggs', 'milk', 'cheese']

print("a;b;c".split(";"))  # ['a', 'b', 'c']
print("abbaabba".split("ba"))  # ['ab', 'ab', '']

# Ways to create lists
# 1. A list literal
# 2. The list() built-in
# 3. The string .split() method

# Basic list operations
numbers = [1, 2, 3, 4]
print(numbers[1])  # 2
print(numbers[1:3])  # [2, 3]
print("Bob" in numbers)  # False
for number in numbers:
    if number % 2 == 0:
        print(number)  # 4

# Major difference between tuples and lists is immutability. Elements in lists are mutable while in tuples are immutable.
colors = ["red", "yellow", "green", "blue"]
print(colors)  # ['red', 'yellow', 'green', 'blue']
colors[0] = "burgundy"
print(colors)  # ['burgundy', 'yellow', 'green', 'blue']
colors[1:3] = ["orange", "magenta"]
print(colors)  # ['burgundy', 'orange', 'magenta', 'blue']
colors = ["red", "yellow", "green", "blue"]
print(colors)  # ['red', 'yellow', 'green', 'blue']
colors[1:3] = ["orange", "magenta", "aqua"]
print(colors)  # ['red', 'orange', 'magenta', 'aqua', 'blue']
colors[1:4] = ["yellow", "green"]
print(colors)  # ['red', 'yellow', 'green', 'blue']
"""
The values "yellow" and "green" replace the values "orange" and
"magenta" in colors at the indices 1 and 2. Then the value at index 3 is
replaced with the value "blue". Finally, the slot at index 4 is removed
from colors entirely.
"""

# List Methods for Adding and Removing elements
colors.insert(1, "orange")
print(colors)  # ['red', 'orange', 'yellow', 'green', 'blue']
"""
When the value "orange" is inserted at the index 1, the
value "yellow" and all following values are shifted to the right.
"""
colors.insert(10, "violet")
print(colors)  # ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
colors.insert(-1, "indigo")  # same as colors.insert(len(colors) - 1, "indigo")
print(colors)  # ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

color = colors.pop()
print(color)  # violet
color = colors.pop(3)
print(color)  # green
print(colors)  # ['red', 'orange', 'yellow', 'blue', 'indigo']
color = colors.pop(-1)  # same as colors.pop(len(colors) - 1)
print(color)  # indigo


colors.append("indigo")  # adds indigo to the end of the list
print(colors)  # ['red', 'orange', 'yellow', 'blue', 'indigo']


colors.extend(["violet", "ultraviolet"])
print(colors)  # ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet', 'ultraviolet']
colors.extend(("magenta", "cyan"))
print(
    colors
)  # ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet', 'ultraviolet', 'magenta', 'cyan']


# List comprehensions is a short-hand for a for loop
numbers = (1, 2, 3, 4, 5)
squares = [num**2 for num in numbers]
print(squares)  # [1, 4, 9, 16, 25]

str_numbers = ["1.5", "2.3", "5.25"]
float_numbers = [float(value) for value in str_numbers]
print(float_numbers)  # [1.5, 2.3, 5.25]


# ====== Review exercises ====================================================
# 1. Create a list named food with two elements "rice" and "beans".

# using a list literal
food = ["rice", "beans"]
print(food)  # ['rice', 'beans']

# from a tuple
food = list(("rice", "beans"))
print(food)  # ['rice', 'beans']


# 2. Append the string "broccoli" to food using .append().
food.append("brocolli")
print(food)  # ['rice', 'beans', 'brocolli']


# 3. Add the string "bread" and "pizza" to "food" using .extend().
food.extend(["bread", "pizza"])  # or food.extend(("bread", "pizza"))
print(food)  # ['rice', 'beans', 'brocolli', 'bread', 'pizza']


# 4. Print the ﬁrst two items in the food list using print() and slicing
# notation.
print(food[0:2])  # ['rice', 'beans']
print(food[-5:-3])  # ['rice', 'beans']

# 5. Print the last item in food using print() and index notation.
print(food[-1])  # pizza

# 6. Create a list called breakfast from the string "eggs, fruit, orange
# juice" using the string .split() method.
breakfast = "eggs, fruit, orange juice".split(", ")
print(breakfast)  # ['eggs', 'fruit', 'orange juice']


# 7. Verify that breakfast has three items using len().
print(len(breakfast) == 3)  # True


# 8. Create a new list called lengths using a list comprehension that contains
#  the lengths of each string in the breakfast list.
lengths = [len(item) for item in breakfast]
print(lengths)  # [4, 5, 12]

# ===========End Of Review Exercises ========================================

# Nesting, Copying, and Sorting Tuples and Lists
two_by_two = [[1, 2], [3, 4]]
print(len(two_by_two))  # 2
print(two_by_two[0])  # [1, 2]
print(two_by_two[1])  # [3, 4]
print(two_by_two[0][1])  # 2

animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals
large_cats.append("Tiger")
print(animals)  # ['lion', 'tiger', 'frumious Bandersnatch', 'Tiger']

large_cats = animals[:]
large_cats.append("leopard")
print(large_cats)  # ['lion', 'tiger', 'frumious Bandersnatch', 'Tiger', 'leopard']
print(animals)  # ['lion', 'tiger', 'frumious Bandersnatch', 'Tiger']
large_cats[3] = "jaguar"
print(large_cats)  # ['lion', 'tiger', 'frumious Bandersnatch', 'jaguar', 'leopard']
print(animals)  # ['lion', 'tiger', 'frumious Bandersnatch', 'Tiger']

"""
A shallow copy means constructing a new collection object and then populating
it with references to the child objects found in the original. In essence, a
shallow copy is only one level deep. The copying process does not recurse and
therefore won’t create copies of the child objects themselves.

A deep copy makes the copying process recursive. It means first constructing a
new collection object and then recursively populating it with copies of the
child objects found in the original. Copying an object this way walks the
whole object tree to create a fully independent clone of the original object
and all of its children.
"""
matrix1 = [[1, 2], [3, 4]]
matrix2 = matrix1[:]  # creates a new reference with copies of the original
# matrix1 contents. Shallow copying is onlw one level deep.
matrix2[0] = [
    5,
    6,
]  # replacing the copied child object(reference) with a new object(reference)
print(matrix2)  # [[5, 6], [3, 4]]
print(matrix1)  # [[1, 2], [3, 4]]
matrix2[1][0] = 1
print(matrix2)  # [[5, 6], [1, 4]]
print(matrix1)  # [[1, 2], [1, 4]]
matrix2[0][1] = 3
print(matrix2)  # [[5, 3], [1, 4]]
print(matrix1)  # [[1, 2], [1, 4]]

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # make a shallow copy
# This means ys will now be a new and independent object with the same
# contents as xs
print(xs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(ys)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
xs.append(["new sublist"])
print(xs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
print(ys)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
xs[1][0] = "X"
print(xs)  # [[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new sublist']]
print(ys)  # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
ys[1][1] = "Y"
print(ys)  # [[1, 2, 3], ['X', 'Y', 6], [7, 8, 9]]
print(xs)  # [[1, 2, 3], ['X', 'Y', 6], [7, 8, 9], ['new sublist']]

"""
Making Deep copies
"""
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
print(xs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(zs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
xs[1][0] = "X"
print(xs)  # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
print(zs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
Copying arbitrary objects. How do we create copies (shallow and deep)
of arbitrary objects, including custom classes.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r},{self.y!r})"


a = Point(23, 42)
b = copy.copy(a)
print(a)  # Point(23,42)
print(b)  # Point(23,42)
print(a is b)  # False


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return f"Rectangle({self.topleft!r}, " f"{self.bottomright!r})"


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
print(rect)  # Rectangle(Point(0,1), Point(5,6))
print(srect)  # Rectangle(Point(0,1), Point(5,6))
print(rect is srect)  # False

# Sorting lists
colors = ["red", "yellow", "green", "blue"]
colors.sort()
print(colors)  # ['blue', 'green', 'red', 'yellow']
numbers = [1, 10, 5, 3]
numbers.sort()
print(numbers)  # [1, 3, 5, 10]
colors.sort(key=len)  # sort based on length
print(colors)  # ['red', 'blue', 'green', 'yellow']


def get_second_element(item):
    return item[1]


items = [(4, 1), (1, 2), (-9, 0)]
items.sort(key=get_second_element)
print(items)  # [(-9, 0), (4, 1), (1, 2)]

# ======= Review Exercises =====================

# 1. Create a tuple data with two values. The ﬁrst value should be the
# tuple (1, 2) and the second value should be the tuple (3, 4).
data = ((1, 2), (3, 4))
# 2. Write a for loop that loops over data and prints the sum of each
# nested tuple. The output should look like this:
# Row 1 sum: 3
# Row 2 sum: 7
index = 1
for nums in data:
    print(f"Row {index} sum: {sum(nums)}")
    index += 1

# 3. Create the following list [4, 3, 2, 1] and assign it to the variable
nums = [4, 3, 3, 1]
# 4. Create a copy of the numbers list using the [:] slicing notation.
another_nums = nums[:]
print(another_nums)  # [4, 3, 3, 1]
# 5. Sort the numbers list in numerical order using the .sort() method.
nums.sort()
print(nums)  # [1, 3, 3, 4]

# Challenge: List of lists
# Write a program that contains the following lists of lists:
# universities = [
# ['California Institute of Technology', 2175, 37704],
# ['Harvard', 19627, 39849],
# ['Massachusetts Institute of Technology', 10566, 40732],
# ['Princeton', 7802, 37000],
# ['Rice', 5879, 35551],
# ['Stanford', 19535, 40569],
# ['Yale', 11701, 40500]
# ]
# Deﬁne a function, enrollment_stats(), that takes, as an input, a list of
# lists where each individual list contains three elements: (a) the name
# of a university, (b) the total number of enrolled students, and (c) the
# annual tuition fees.
# enrollment_stats() should return two lists: the ﬁrst containing all of
# the student enrollment values and the second containing all of the
# tuition fees.
# Next, deﬁne a mean() and a median() function. Both functions should
# take a single list as an argument and return the mean and median of
# the values in each list.
# Using universities, enrollment_stats(), mean(), and median(), calculate
# the total number of students, the total tuition, the mean and median
# of the number of students, and the mean and median tuition values.
# Finally, output all values, and format the output so that it looks like
# this:
# ******************************
# Total students:77,285
# Total tuition:$ 271,905
# Student mean:11,040.71
# Student median:10,566
# Tuition mean:$ 38,843.57
# Tuition median: $ 39,849
# ******************************

universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]

"""
Takes as input a list of lists where each individual list  contains three 
elements:
(a) the name of a university
(b) the total number of enrolled students, and
(c) the annual tuition fees
and returns two lists: the first containing all of the student enrollment 
values and the second containing all of the tuition fees.
"""


def enrollment_stats(universities):
    student_enrollment, tuition_fees = [], []
    for university in universities:
        student_enrollment.append(university[1])
        tuition_fees.append(university[2])
    return student_enrollment, tuition_fees


def mean(a_list):
    try:
        return sum(a_list) / len(a_list)
    except Exception as e:
        raise Exception(e)


def median(a_list):
    try:
        a_list.sort()
        middle = len(a_list) / 2
        return a_list[int(middle)]
    except Exception as e:
        raise Exception(e)


student_enrollment, tuition_fees = enrollment_stats(universities)
total_enrollment = sum(student_enrollment)
total_fees = sum(tuition_fees)
student_mean = mean(student_enrollment)
student_median = median(student_enrollment)
tuition_mean = mean(tuition_fees)
tuition_median = median(tuition_fees)
print("********************************************")
print()
print(f"Total students:    {total_enrollment:,}")
print()
print(f"Total tuition:   $ {total_fees:,}")
print()
print()
print(f"Student mean:      {student_mean:,.2f}")
print()
print(f"Student median:    {student_median:,}")
print()
print()
print(f"Tuition mean:    $ {tuition_mean:,.2f}")
print()
print(f"Tuition median:  $ {tuition_median:,}")
print()
print("********************************************")

#
# 9.5 Challenge: Wax Poetic
#
# In this challenge, you’ll write a program that generates poetry.
# Create ﬁve lists for diﬀerent word types: nouns, verbs, adjectives,
# prepositions, adverbs.
# Randomly select the following number of elements from each list:
# - 3 nouns
# - 3 verbs
# - 3 adjectives
# - 2 prepositions
# - 1 adverb
# You can do this with the choice() function in the random module. This
# function takes a list as input and returns a randomly selected element
# of the list.
# For example, here’s how you use random.choice() to get random element from
# the list ["a", "b", "c"]:
# Using the randomly selected words, generate and display a poem with
# the following structure inspired by Cliﬀord Pickover:
# {A/An} {adj1} {noun1}
# {A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
# {adverb1}, the {noun1} {verb2}
# the {noun2} {verb3} {prep2} a {adj3} {noun3}
# Here, adj stands for adjective and prep for preposition.
# Here’s an example of the kind of poem your program might generate:
# A furry horse
# A furry horse curdles within the fragrant mango
# extravagantly, the horse slurps
# the mango meows beneath a balding extrovert
# Every time your program runs, it should generate a new poem.
nouns = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
random_nouns = [random.choice(nouns) for i in range(3)]
random_verbs = [random.choice(verbs) for i in range(3)]
random_adjectives = [random.choice(adjectives) for i in range(3)]
random_prepositions = [random.choice(prepositions) for i in range(3)]
random_adverb = random.choice(adverbs)
print(f"A/An {random_adjectives[0]} {random_nouns[0]}")
print(
    f"A/An {random_adjectives[0]} {random_nouns[0]} {random_verbs[0]} {random_prepositions[0]} the {random_adjectives[1]} {random_nouns[1]}"
)
print(f"{random_adverb}, the {random_nouns[0]} {random_verbs[1]}")
print(
    f"the {random_nouns[1]} {random_verbs[2]} {random_prepositions[1]} a {random_adjectives[2]} {random_nouns[2]}"
)
