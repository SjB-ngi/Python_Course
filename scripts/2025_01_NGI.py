"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in October
2025 in 4x4 hour sessions.

This script contains the code that was written during the first session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 1 on 6th of October 2025
###########################

### introduction and overview over Spyder


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




# Exercise 1

### operators: +, -, /, *, **, //, %


# Exercise 2


### variables, string formatting

# Variables can be assigned data by setting them equal to a value
# python automatically assigns a data type to the variable


# You may also assign multiple variables respectively using comma. The code
# below assigns the value of 1 to variable a and the value of 2 to variable b


# variable names should be explicit and informative


# These variables will be used in the following examples


# There are multiple ways to format a string

# string concatenation: "string" + "another string"


# .format() function replaces the {} with the function inputs
# The string may be stored as a variable. We can add multiple inputs
# to .format()


# f-strings are assigned by adding the character f before the string
# These are useful for having a good idea about what you're printing


# formatting strings is useful when working with or saving multiple images.
# Here we can use some info to give file names to our images.



### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# The list is defined using square brackets


# You may access the values of the list (indexing the list) a list by using 
# integers in square brackets directly following the variable name of the list
# Indexing starts at 0, (i.e. the first entry is at index 0, the second at index 1, etc.)


# You may add data to the list by using the .append() function


# You can find the amount of entries of a list using len()


# You can slice a list by using colons, it returns a list
# from (and including) the index 0 to, but not including
# index 2


# You may assign a new value to an entry of the list by using the index



# Tuples act similarly to lists in many ways, but cannot change
# after assignment. Tuples are defined by using regular parentheses


# since the tuple cannot be changed, the following line would throw an error
# ucs_tuple.append(78)


# Dictionaries store data in an unstructured way
# These are indexed using keys (strings)

# Dictionaries are defined by using curly brackets
# Key and value pairs are separated by colon, entries
# are separated with a comma. The values can be any data type



# The values of a dictionary do not need to be strings
# they can be any data type, like lists


# We can use the value of a dictionary item by indexing it with the key


# Lets try to append a value to the list of UCS values for limestone


# We can now look at the final value of the list of UCS values for limestone
# by indexing the dictionary with the key "limestone" and the list with -1


# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1


# you can set the starting number and the step size similarly
# to how we slice lists (start, stop, step)



# Exercise 3

# It's normal practice to start with an empty list and append values to it


# We can use the len() function to find the length of a string
# and append it to the list


# Here I use the sum() function to sum the last three entries of the list


# Here we print the result by formatting a string in two different ways


# Exercise 4


# First we print the first two entries of the list and tuple


# We try to append a new entry to the list and tuple
# This will work for the list, but throw an error for the tuple



# Now we try to change the second entry of the list and tuple
# This will work for the list, but throw an error for the tuple

