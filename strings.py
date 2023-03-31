#!/usr/bin/env python3

# =================Review Exercise=================
quote = '"He who believes in himself has already won the battle", said Muhammad Ali'
print(quote)
quote = "I don't know how I am going to do it, but I will just try"
print(quote)
docString = """
 This is a string that spans multiple lines with whitespace reseved

 Such a string is commonly used for documentation purposes.
"""
print(docString)
code = "This is a string that is coded on multiple lines but displayed \
on a single line"
print(code)

# ========== End of Review Exercise ========

first_name = "Arthur"
last_name = "Dent"
fullname = first_name + " " + last_name
print(fullname)

# string indexing
flavor = "apple pie"
print(flavor[1])
print(f"{len(flavor)}")
print(flavor[-1])  # similar to flavor[len(flavor) - 1]

# string slicing
print(flavor[0:3])  # app
print(flavor[:3])  # app
print(flavor[6:])  # pie
print(flavor[:])  # apple pie
"""
python throws away any non-existent indices and the entire string 'apple pie' is returned.
"""
print(flavor[:14])  # apple pie
"""
below we attempt to get the thirteenth and fourteenth characters, which don’t exist
Instead of raising an error, the empty string "" is returned
"""
print(flavor[13:15])  # '' prints empty string
print(flavor[-9:-6])  # same to flavor[len(flavor)-9: len(flavor)-6] = app
print(flavor[-9:0])  # ''
print(flavor[-10:-1])

# =============== Review Exercise ======================
# 1. Create a string and print its length using the len() function.
str = "this is a string"
print(len(str))
# 2. Create two strings, concatenate them, and print the resulting string.
str_a = "first"
str_b = "second"
str_c = str_a + str_b
print(str_c)
# 3. Create two strings and use concatenation to add a space in- between them. Then print the result.
first = "firstname"
second = "lastname"
result = first + " " + second
print(result)
# 4. Print the string "zing" by using slice notation on the string "bazinga" to specify the correct range of characters.
str = "bazinga"
print(str[2:6])  # zing
print(str[-5:-1])  # zing

# ========== End of Review Exercise ========


# string manipulation
loud_voice = "Can you hear me?"
print(loud_voice.upper())

name = "mwangi     "
print(f'"{name}"')
print(f'"{name.rstrip()}"')
name = " mwangi "
print(f'"{name}"')
print(f'"{name.lstrip()}"')
print(f'"{name.strip()}"')

starship = "Enterprise"
print(starship.startswith("en"))
print(starship.startswith("En"))
print(starship.endswith("rise"))
print(starship.endswith("riSE"))

name = "Picard"
name = name.upper()
print(name)

# ================ Review Exercises ===========================
# 1. Write a script that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honeybadger".
#    Print each lowercase string on a separate line.
words = ["Animals", "Badger", "Honey Bee", "HoneyBadger"]
# solution 1
for word in words:
    print(word.lower())

# solution 2
for i in range(len(words)):
    print(words[i].lower())

# 2. Repeat Exercise 1, but convert each string to uppercase instead of lowercase.
# solution 1
for word in words:
    print(word.upper())

# solution 2
for i in range(len(words)):
    print(words[i].upper())

# 3. Write a script that removes whitespace from the following strings:
string1 = "    Filet Mignon"
string2 = "Brisket    "
string3 = "  Cheeseburger   "
# Print out the strings with the whitespace removed.
print(f'"{string1.lstrip()}"')
print(f'"{string2.rstrip()}"')
print(f'"{string3.strip()}"')
# 4. Write a script that prints out the result of .startswith("be") on each
# of the following strings:
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "  bEautiful"
# solution
print(string1.startswith("be"))  # False
print(string2.startswith("be"))  # True
print(string3.startswith("be"))  # False
print(string4.startswith("be"))  # False

# 5. Using the same four strings from Exercise 4, write a script that
# uses string methods to alter each string so that .startswith("be")
# returns True for all of them.
# solution
string1 = string1.lower()
string3 = string3.lower()
string4 = string4.lstrip().lower()

print(string1.startswith("be"))  # True
print(string2.startswith("be"))  # True
print(string3.startswith("be"))  # True
print(string4.startswith("be"))  # True

# ======== End of Review Exercise ===============

# String formatting
errno = 50159747054
name = "Bob"

"""
 Old style string formatting
"""
print("Hello, %s" % name)  # Hello, Bob
# %x format specifier to convert an int to string and to represent it as a
# hexadecimal number:
print("%x" % errno)  # badc0ffee
# The “old style” string formatting syntax changes slightly if you want to
# make multiple substitutions in a single string. Because the % operator takes
#  only one argument, you need to wrap the right-hand side in a tuple, like so:
print(
    "Hey %s, there is a 0x%x error!" % (name, errno)
)  # Hey Bob, there is a 0xbadc0ffee error!
# It’s also possible to refer to variable substitutions by name in your format
#  string, if you pass a mapping to the % operator:
print(
    "Hey %(name)s, there is a 0x%(errno)x error!" % {"name": name, "errno": errno}
)  # Hey Bob, there is a 0xbadc0ffee error!

"""
New style string formatting
"""
print("Hello, {}".format(name))  # Hello, Bob
print(
    "Hey {name}, there is a 0x{errno:x} error!".format(name=name, errno=errno)
)  # Hey Bob, there is a 0xbadc0ffee error!
# In the above example, you need to pass a format spec by adding a :x suffix.

# string interpolation/ f-Strings (python 3.6+)
print(f"Hello, {name}")
a = 5
b = 10
print(f"Five plus ten is {a+b} and not {2 * (a+b)}.")  # Five plus ten is 15 and not 30.

# Template strings (standard library)
from string import Template  # noqa: E402

t = Template("Hey, $name!")
print(t.substitute(name=name))  # Hey, Bob!
templ_string = "Hey $name, there is a $error error!"
print(
    Template(templ_string).substitute(name=name, error=hex(errno))
)  # Hey Bob, there is a 0xbadc0ffee error!

# Example of how a malicious user can supply a malicious format string, and
# potentially leak secret keys

# This is out super secret key:
SECRET = "this-is-a-secret"


class Error:
    def __init__(self):
        pass


# A malicious user can craft a format string that
# can read data from the global namespace:
user_input = "{error.__init__.__globals__[SECRET]}"
err = Error()
print(user_input.format(error=err))  # this-is-a-secret

# Template strings close this attack vector. This makes them a safer choice
# if you’re handling format strings generated from user input:
user_input = "${error.__init__.__globals__[SECRET]}"
print(
    Template(user_input).substitute(error=err)
)  # ValueError: Invalid placeholder in string: line 1, col 1
