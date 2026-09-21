"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in September
2026 in 4x4 hour sessions.

This script contains the code that was written during the first session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Modifications: Sjur Beyer, sjur.beyer@ngi.no
Author: Dr. Georg H. Erharter
"""

###########################
# session 1 on 15th of September 2026
###########################

# introduction and overview over uv and VS Code


### basic datatypes: strings, integers, floats, print function

# Datatypes

# integer numbers are represented with an "int" data type
1
2
3
# In a script these expressions do not print anything by themselves. In an
# interactive console, the value of the last expression is displayed.

# decimal numbers are represented with a "float" data type
1.2

# text is represented with a "str" data type
# "str" is short for string, or string of characters
# you may use either double quotes, ", single quotes, ', or
# tripled double or single quotes, """ / ''', to construct
# a string

"Double quotes"
'single quotes'
# Both strings contain text, and both have the data type "str".

# You may use triple quotes to write long strings over multiple lines

"""
This string
Can go across multiple lines
"""
# The line breaks are part of this string.

# You can print the data to the console by using the print() function
1+1
print(1+1)
# The first expression is only shown in an interactive console; print() shows
# the result when the file is run as a script.

# You may check the datatype by using the type() function, if you want
# to see the results, you have to print it out
print(type(1.2))


# you can change the data type by using the int(), float() and str()
# functions. Data might get lost in the process
print(int(1.8))
# returns 1, an integer; the decimal part is lost

### operators: +, -, /, *, **, //, %
# The operators below perform addition, subtraction, division, and
# multiplication respectively.
print(1+1)  # Addition
print(3-2)  # Subtraction
print(1/2)  # Division
print(2*4)  # Multiplication
print(2**3) # Exponentiation


# Integer division, floored division
print(7//2)
# returns 3; the decimal part is discarded

# Modulo, remainder
print(9%3)
# returns 0, the remainder after division

# Note that the + operator works differently for strings and numbers
print("1"+"1")
# returns '11', a string

# Exercise 1
print("Hello World!")

print()
# Exercise 2
print(5**8)
# 5 to the power of 8
print(9**0.5)
# the square root of 9
print(14%5)
# the remainder of 14 divided by 5
print(13//3*3)
# the product of the floored division of 13 by 3 and 3

### variables, string formatting

# Variables can be assigned data by setting them equal to a value
# python automatically assigns a data type to the variable
print()
abc = 12

print(type(abc))
# abc is an integer here, so this prints <class 'int'>

abc = 23.2

print(type(abc))
# abc now refers to a float, so this prints <class 'float'>

# variable names should be explicit and informative
UCS_sand = 12
# The value is an unconfined compressive strength in MPa.

lab_test = "UCS"
test_name = "Test1"
image_type = ".jpg"

# There are multiple ways to format a string, we focus on two

# string concatenation: "string" + "another string"
image_name = lab_test + "_" + str(test_name) + image_type
print(image_name)
# str() converts a value to text so it can be joined with other strings


# f-strings are assigned by adding the character f before the string
# These are useful for having a good idea about what you're printing
image_name = f"{lab_test}_{test_name}{image_type}"
print(image_name)
# f-strings insert the values of variables inside curly brackets

# formatting strings is useful when working with or saving multiple files.
# Here we can use some info to give file names to our images.


### datatypes: lists, dictionaries, indices, exceptions / errors

# The list is defined using square brackets []
test_locations = [1, 2, 3, 5]

# You may access the values of the list (indexing the list) a list by using 
# integers in square brackets directly following the variable name of the list
# Indexing starts at 0, (i.e. the first entry is at index 0, the second at index 1, etc.)
print(test_locations[0])
# returns the first element, 1
print(test_locations[1])
# returns the second element, 2
print(test_locations[-1])
# returns the last element, 5

# You may add data to the list by using the .append() function
test_locations.append(6)
# The list now contains one additional element.

print(test_locations)

# You can find the amount of entries of a list using len()
print(len(test_locations))
# returns 5

# You can slice a list by using colons, it returns a list
# from (and including) the index 0 to, but not including index 2

print(test_locations[0:2])
# returns [1, 2]; index 2 is not included

# You may assign a new value to an entry of the list by using the index
test_locations[2] = 4
# The third element is now 4 instead of 3.

print(test_locations)

# Dictionaries store data in an unstructured way
# These are indexed using keys (strings)

# Dictionaries are defined by using curly brackets
# Key and value pairs are separated by colon, entries
# are separated with a comma. The values can be any data type
test_location_dict = {}
# This creates an empty dictionary.

test_location_dict["Location 1"] = "Refraction"
test_location_dict["Location 2"] = {"PSD": [0.1, 0.9]}
test_location_dict["Location 2"] = "CPT"  # <- Overwrites the data in "Location 2"
test_location_dict["Location 3"] = [1, 2, 3]
# A dictionary entry is created by assigning a value to a key.

print(test_location_dict)

# We can use the value of a dictionary item by indexing it with the key
print(test_location_dict["Location 2"])
# returns "CPT"

# Lets try to append a value to the list belonging to Location 3
test_location_dict["Location 3"].append(4)
# The list stored as the value for Location 3 now ends in 4.

print(test_location_dict)

print(test_location_dict.keys())
# returns a view containing the dictionary keys

# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1
print(list(range(0, 5)))
# returns [0, 1, 2, 3, 4]

# you can set the starting number and the step size similarly
# to how we slice lists (start, stop, step)
print(list(range(0, 10, 2)))
# returns [0, 2, 4, 6, 8]

# Exercise 3
print()

# We first instantiate an empty list
character_len_list = []

# Here we append the lengths of the rock names using len()
character_len_list.append(len("marl"))
character_len_list.append(len("gneiss"))
character_len_list.append(len("limestone"))
character_len_list.append(len("eclogite"))

# We print the list of character counts
print(character_len_list)

# We sum the last three elements by indexing them individually
last_three_sum = character_len_list[-3] + character_len_list[-2] + character_len_list[-1]

# Alternatively, we can use sum() on a slice containing the last three elements
last_three_sum = sum(character_len_list[-3:]) # Alternative

# Then we print the result using an f-string
print(f"the result is: {last_three_sum}")


# Exercise 4
# We instantiate a list of rock names.
rock_list = ["gneiss", "marl", "limestone"]

# A slice returns a new list containing the first two elements.
rock_slice = rock_list[0:2]
print(rock_slice)
# returns ['gneiss', 'marl']

# We append an element to the end of the slice.
rock_slice.append("greenschist")

# We replace the second element of the slice.
rock_slice[1] = "dolomite"

# The original rock_list is unchanged; the edits were made to rock_slice.
print(rock_slice)
# returns ['gneiss', 'dolomite', 'greenschist']


### Boolean operators: or, and, not
# These are used to do operations on True/False data, i.e boolean data

# Boolean values are written as capitalized words:
True # 1
# True is the boolean value for a condition that is fulfilled.

False # 0
# False is the boolean value for a condition that is not fulfilled.


# We can turn other datatypes into boolean values by using the bool() function
# Non-zero numbers and non-empty strings are True, zero and empty strings are False
print(bool(0))
# returns False

# "not" is used to reverse a boolean value
print(not True)
# returns False


# "or" is used to check if at least one of the two boolean values is True
print(True or False)
# returns True
print(False or False)
# returns False
print(False or True)
# returns True

# "and" is used to check if both boolean values are True
print(True and False)
# returns False
print(True and True)
# returns True
print(False and False)
# returns False


# comparison operators: <, >, <=, >=, ==, !=
# These are used to compare two values, and return a boolean value
print(1<3)
# less than; returns True

print(3==3)
# is equal to; returns True

print(1!=3)
# is not equal to; returns True


### conditional statements: if, elif, else

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False

if image_type == ".png":
    # Inside of the if block
    print("This is a png image")
# image_type is ".jpg", so this block is skipped

# More code
print("loading image")

# Only if the expression after if is True, the code in the indentation block
# will be executed
# The code after the if block is not indented, so it always runs.


# Elif can be used for additional tests, only if the first if statement
# is False
if image_type == ".png":
    print("This is a png image")
elif image_type == ".gif":
    print("This is a gif image")

# Since image_type is neither ".png" nor ".gif", the else block runs.

# Else is used if none of the previous if or elif statements were True
if image_type == ".png":
    print("This is a png image")
elif image_type == ".gif":
    print("This is a gif image")
else:
    print("Not recognized image type")

# In the case where you have multiple conditions to check, you can use
# multiple elif statements
if image_type == ".png":
    print("This is a png image")
elif image_type == ".gif":
    print("This is a gif image")
elif image_type == ".jpg":
    print("This is a jpg image")
else:
    print("Not recognized image type")


