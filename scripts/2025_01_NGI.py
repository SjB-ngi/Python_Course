# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in May 2025 in 4x4 hour sessions.

This script contains the code that was written during the first session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 1 on 5th of May 2025
###########################

### introduction and overview over Spyder


### basic datatypes: strings, integers, floats, print function

# Datatypes

# integer numbers are represented with an "int" data type
1, 2, 3

# decimal numbers are represented with a "float" data type
1.2, 3.7, 4.2

# text is represented with a "str" data type
# "str" is short for string, or string of characters
# you may use either double quotes, ", single quotes, ', or
# tripled double or single quotes, """ / ''', to construct
# a string
"informative text", 'sample ID', '''formation name'''

# You may use triple quotes to write long strings over multiple lines
"""
A chapter from your favorite book

"""

# You can print the data to the console by using the print() function
print("text to output to the console")

# You may check the datatype by using the type() function, if you want
# to see the results, you have to print it out

print(type(1))
# returns int

print(type(1.0))
# returns float

print(type("1"))
# returns str


# you can change the data type by using the int(), float() and str()
# functions. Data might get lost in the process

int("1")
# returns 1

float("1")
# returns 1.0

str(1)
# returns "1"


# Exercise 1
print("Hello world")  # In the exercise, this should be printed from the console


### operators: +, -, /, *, **, //, %
print(1 + 1)  # addition
print(1 - 1)  # subtraction
print(2 * 2)  # multiplication
print(12 / 3)  # division
print(4**2)  # exponentiation (to the power of)
print(13 // 4)  # floored division / integer division
print(5 % 2)  # modulo / remainder


# Exercise 2

# 5 to the power of 8
print(5 ** 8)
# prints 390625

# square root of 9
print(9 ** 0.5)
# prints 3.0

# remainder of 14 divided by 5
print(14 % 5)
# prints 4

# product of the integer division of 13 and 3 with 3
print(13 // 3 * 3)
# prints 12


### variables, string formatting

# Variables can be assigned data by setting them equal to a value
# python automatically assigns a data type to the variable
variable_name = "variable value"
numerical_variable = 2

# You may also assign multiple variables respectively using comma. The code
# below assigns the value of 1 to variable a and the value of 2 to variable b
a, b = 1, 2

# variable names should be explicit and informative
formation_bottom = 34

# These variables will be used in the following examples
limestone_ucs = 90
unit = "MPa"
rock_type = "limestone"


# There are multiple ways to format a string

# string concatenation: "string" + "another string"
print("The UCS of the " + rock_type + " is " + str(limestone_ucs) + " " + unit)

# .format() function replaces the {} with the function inputs
# The string may be stored as a variable. We can add multiple inputs
# to .format()
print("The UCS of the {} is {} {}".format(rock_type, limestone_ucs, unit))

# f-strings are assigned by adding the character f before the string
# These are useful for having a good idea about what you're printing
print(f"The UCS of the {rock_type} is {limestone_ucs} {unit}")

# formatting strings is useful when working with or saving multiple images.
# Here we can use some info to give file names to our images.
filename = f"C:/Users/participant/rock_images/{rock_type}_{limestone_ucs}{unit}.jpg"


### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# The list is defined using square brackets
ucs_list = [86, 98, 89, 68]

# You may access the values of the list (indexing the list) a list by using 
# integers in square brackets directly following the variable name of the list
# Indexing starts at 0, (i.e. the first entry is at index 0, the second at index 1, etc.)
print(ucs_list[0])
print(ucs_list[1])
print(ucs_list[-1])  # negative indices count from the end of the list
print(ucs_list[-2])  # -1 is the last entry, -2 is the second to last entry

# You may add data to the list by using the .append() function
ucs_list.append(78)
print(ucs_list)

# You can find the amount of entries of a list using len()
print(len(ucs_list))

# You can slice a list by using colons, it returns a list
# from (and including) the index 0 to, but not including
# index 2
print(ucs_list[0:2])  # returns [86, 98]

# You may assign a new value to an entry of the list by using the index
ucs_list[1] = 90


# Tuples act similarly to lists in many ways, but cannot change
# after assignment. Tuples are defined by using regular parentheses
ucs_tuple = (86, 98, 89, 68)

# since the tuple cannot be changed, the following line would throw an error
# ucs_tuple.append(78)


# Dictionaries store data in an unstructured way
# These are indexed using keys (strings)

# Dictionaries are defined by using curly brackets
# Key and value pairs are separated by colon, entries
# are separated with a comma. The values can be any data type

book_authors = {"harry potter": "J. K. Rowling", "lord of the rings": "J.R.R. Tolkien"}

# The values of a dictionary do not need to be strings
# they can be any data type, like lists

rock_ucs_dict = {"limestone": [86, 98, 89, 68], "sandstone": [90, 89]}

# We can use the value of a dictionary item by indexing it with the key
rock_ucs_dict["limestone"]  # returns the list of UCS values for limestone

# Lets try to append a value to the list of UCS values for limestone
rock_ucs_dict["limestone"].append(78)

# We can now look at the final value of the list of UCS values for limestone
# by indexing the dictionary with the key "limestone" and the list with -1
print(rock_ucs_dict["limestone"][-1])

# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1
print(list(range(10)))
# prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# you can set the starting number and the step size similarly
# to how we slice lists (start, stop, step)
print(list(range(5, 10, 2)))
# prints: [5, 7, 9]


# Exercise 3

# It's normal practice to start with an empty list and append values to it
rock_character_lengths = []

# We can use the len() function to find the length of a string
# and append it to the list
rock_character_lengths.append(len("marl"))
rock_character_lengths.append(len("gneiss"))
rock_character_lengths.append(len("limestone"))
rock_character_lengths.append(len("eclogite"))

print(rock_character_lengths)

# Here I use the sum() function to sum the last three entries of the list
rock_character_sum = sum(rock_character_lengths[-3:])

# Here we print the result by formatting a string in two different ways
print("the result is: {}".format(rock_character_sum))
print(f"the result is: {rock_character_sum}")


# Exercise 4

rock_list = ["gneiss", "marl", "limestone"]
rock_tuple = ("gneiss", "marl", "limestone")

# First we print the first two entries of the list and tuple
print(rock_list[:2])
print(rock_tuple[:2])

# We try to append a new entry to the list and tuple
# This will work for the list, but throw an error for the tuple

rock_list.append("greenschist")
# rock_tuple.append("greenschist")

# Now we try to change the second entry of the list and tuple
# This will work for the list, but throw an error for the tuple
rock_list[1] = "dolomite"
# rock_tuple[1] = "dolomite"
