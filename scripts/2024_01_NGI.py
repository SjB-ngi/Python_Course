# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in November to
December 2024 in 4x4 hour sessions.

This script contains the code that was written during the first session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 1 on 25th of November 2024
###########################

### introduction and overview over Spyder


### basic datatypes: strings, integers, floats, print function

# Datatypes

# integer numbers are represented with an "int" data type
1, 2, 3

# decimal numbers are represented with a "float" data type
1.3, 3.7, 4.2

# text is represented with a "str" data type
# "str" is short for string, or string of characters
# you may use either double quotes, ", single quotes, ', or
# tripled double or single quotes, """ / ''', to construct
# a string
"Wednesday", "orange", """wizard"""

# You can print the data to the console by using the print() function
print("wizard")

# You may check the datatype by using the type() function, if you want
# to see the results, you have to print it out
type(1)
# returns int

type(1.0)
# returns float

type("1")
# returns str

# printing the datatype
print(type(1.0))

# you can change the data type by using the int(), float() and str()
# functions. Data might get lost in the process
float("1")
# returns 1.0

int(1.2)
# returns 1

str(1)
# returns "1"


# Exercise 1

### operators: +, -, /, *, **, //, %
print(1 + 3)  # addition
print(3 - 5)  # subtraction
print(12 / 3)  # division
print(2 * 3)  # multiplication
print(4**2)  # to the power of
print(13 // 4)  # floored division / integer division
print(12 % 5)  # modulo / remainder

# Exercise 2

### variables, string formatting


# Variables can be assigned data by setting them equal to a value
# python automatically assigns a data type to the variable
a = 2

name = "Sjur"

b = 13

# You may also assign multiple variables respectively using comma
a, b = 12, 2

# variable names should be explicit and informative
limestone_ucs = 90
rock = "limestone"
unit = "MPa"
image_filename = "C:/Users/SjB/rock_images/{}.jpg"


# There are multiple ways to format a string

# string concatenation: "string" + "another string"
print("The UCS of the limestone is " + str(limestone_ucs) + " MPa")

# .format() function replaces the {} with the function inputs
# (here limestone_ucs)
print("The UCS of the limestone is {} MPa".format(limestone_ucs))

# The string may be stored as a variable. We can add multiple inputs
#  to .format(). This will insert the values in rock, limestone_ucs
# and unit to the first, second and third {} in the string respectively.
user_output = "The UCS of the {} is {} {}"
print(user_output.format(rock, limestone_ucs, unit))

# f-strings are assigned by adding the character f before the string
# These are useful for having a good idea about what you're printing
print(f"The UCS of the {rock} is {limestone_ucs} {unit}")

# formatting strings is useful when working with or saving multiple images.
# Here we can use some info to give file names to our images.
print(image_filename.format(rock + "_" + str(limestone_ucs) + "_" + unit))


### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# The list is defined using square brackets
ucs_list = [85, 92, 78]

# You may index a list by using integers starting at 0
ucs_list[0]  # returns the first element
ucs_list[1]  # returns the second element
ucs_list[-1]  # returns the last element

# You may add data to the list
ucs_list.append(80)  # Adds the value to the end of the list
ucs_list.insert(0, 76)  # Inserts the data to the start (index 0)

# You can find the amount of entries of a list using len()
len(ucs_list)
# returns: 5

# You can slice a list by using colons, it returns a list
# from (and including) the index 0 to, but not including
# index 2
ucs_list[0:2]  # returns the first and second element

# Tuples act similarly to lists in many ways, but cannot change
# after assignment
ucs_tuple = tuple(ucs_list)


# Dictionaries store data in an unstructured way
# These are indexed using keys (strings)

# Dictionaries are defined by using curly brackets
# Key and value pairs are separated by colon, entries
# are separated with a comma. The values can be any data type

rock_ucs_dict = {"limestone": [77, 85, 92, 78, 80], "sandstone": [120], "shale": []}

# We index the "shale" string, this fetches the empty list assigned
# to shale, and adds the value 20 to the end of the list.
rock_ucs_dict["shale"].append(20)

# The values of a dictionary do not need to be lists
# they can be any data type, like strings

book_authors = {"Harry Potter": "J.K. Rowling", "Lord of the rings": "J.R.R Tolkien"}


# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1
print(list(range(10)))
# prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# you can set the starting number and the step size similarly
# to how we slice lists (start, stop, step)
print(list(range(5, 10, 2)))
# prints: [5, 7, 9]

# Exercise 3

# Exercise 4
