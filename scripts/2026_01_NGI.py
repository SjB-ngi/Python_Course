"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in September
2026 in 4x4 hour sessions.

This script contains the code that was written during the first session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 1 on 15th of September 2026
###########################


### introduction and overview over uv and VS Code


### basic datatypes: strings, integers, floats, print function

# Datatypes

# integer numbers are represented with an "int" data type


# decimal numbers are represented with a "float" data type


# text is represented with a "str" data type
# "str" is short for string, or string of characters
# you may use either double quotes, ", single quotes, ', or
# tripled double or single quotes, """ / ''', to construct
# a string


# You may use triple quotes to write long strings over multiple lines


# You can print the data to the console by using the print() function


# You may check the datatype by using the type() function, if you want
# to see the results, you have to print it out


# you can change the data type by using the int(), float() and str()
# functions. Data might get lost in the process


### operators: +, -, /, *, **, //, %


# Note that the + operator works differently for strings and numbers


# Exercise 1


# Exercise 2


### variables, string formatting

# Variables can be assigned data by setting them equal to a value
# python automatically assigns a data type to the variable


# variable names should be explicit and informative


# There are multiple ways to format a string, we focus on two

# string concatenation: "string" + "another string"


# f-strings are assigned by adding the character f before the string
# These are useful for having a good idea about what you're printing


# formatting strings is useful when working with or saving multiple files.
# Here we can use some info to give file names to our images.


### datatypes: lists, dictionaries, indices, exceptions / errors

# The list is defined using square brackets


# You may access the values of the list (indexing the list) a list by using 
# integers in square brackets directly following the variable name of the list
# Indexing starts at 0, (i.e. the first entry is at index 0, the second at index 1, etc.)


# You may add data to the list by using the .append() function


# You can find the amount of entries of a list using len()


# You can slice a list by using colons, it returns a list
# from (and including) the index 0 to, but not including index 2


# You may assign a new value to an entry of the list by using the index


# Dictionaries store data in an unstructured way
# These are indexed using keys (strings)

# Dictionaries are defined by using curly brackets
# Key and value pairs are separated by colon, entries
# are separated with a comma. The values can be any data type


# We can use the value of a dictionary item by indexing it with the key


# Lets try to append a value to the list of UCS values for limestone


# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1


# you can set the starting number and the step size similarly
# to how we slice lists (start, stop, step)



# Exercise 3


# Exercise 4


### Boolean operators: or, and, not
# These are used to do operations on True/False data, i.e boolean data

# Boolean values are written as capitalized words:


# We can turn other datatypes into boolean values by using the bool() function
# Non-zero numbers and non-empty strings are True, zero and empty strings are False


# "not" is used to reverse a boolean value


# "or" is used to check if at least one of the two boolean values is True


# "and" is used to check if both boolean values are True


# comparison operators: <, >, <=, >=, ==, !=
# These are used to compare two values, and return a boolean value


### control structures: conditional statements: if, elif, else

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False


# Only if the expression after if is True, the code in the indentation block
# will be executed


# Elif can be used for additional tests, only if the first if statement
# is False


# Else is used if none of the previous if or elif statements were True


# In the case where you have multiple conditions to check, you can use
# multiple elif statements


