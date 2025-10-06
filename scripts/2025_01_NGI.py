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


### introduction and overview over uv and VS Code


### basic datatypes: strings, integers, floats, print function

# Datatypes

# integer numbers are represented with an "int" data type
print(1)

# decimal numbers are represented with a "float" data type
print(1.2)

# text is represented with a "str" data type
# "str" is short for string, or string of characters
# you may use either double quotes, ", single quotes, ', or
# tripled double or single quotes, """ / ''', to construct
# a string

"string"

'string'

"""string"""

# You may use triple quotes to write long strings over multiple lines
"""I can have line breaks
without ending the string"""

# You can print the data to the console by using the print() function
print(1.2)

# You may check the datatype by using the type() function, if you want
# to see the results, you have to print it out
print(type(1.2))


# you can change the data type by using the int(), float() and str()
# functions. Data might get lost in the process

print(str(1.2))
# returns '1.2', a string

print(int(1.4))
# returns 1, an integer

### operators: +, -, /, *, **, //, %
print(1 + 3)  # addition
print(3 - 5)  # subtraction
print(12 / 3)  # division
print(2 * 3)  # multiplication
print(4**2)  # to the power of
print(13 // 4)  # floored division / integer division
print(12 % 5)  # modulo / remainder

# Note that the + operator works differently for strings and numbers
print("1"+"1")
# returns '11', a string

print(1+1)
# returns 2, an integer


# Exercise 1
print("Hello World!")  # also printing "Hello World!" in the console

# Exercise 2
print(5**8)       # 5 to the power of 8
print(9**0.5)     # square root of 9
print(14 % 5)     # remainder of 14 divided by 5
print((13//3)*3)  # the product of the floored division of 13 by 3 and 3


### variables, string formatting

# Variables can be assigned data by setting them equal to a value
# python automatically assigns a data type to the variable

a = 1

b = 2

# You may also assign multiple variables respectively using comma. The code
# below assigns the value of 1 to variable a and the value of 2 to variable b

a, b = 1, 2

# variable names should be explicit and informative
rock_strenth = 90.0

# These variables will be used in the following examples
# Let's imagine a is a parameter we could adjust for a test,
# and we want to save the results in a file and preserve the
# information about the parameter.
results_name = "test_results"
file_ending = ".xlsx"


# There are multiple ways to format a string

# string concatenation: "string" + "another string"
result_file = results_name + "_a-" + str(a) + file_ending  # Note that we had to convert the integer a to a string using str(a)
print(result_file)

# .format() function replaces the {} with the function inputs
# The string may be stored as a variable. We can add multiple inputs
# to .format()
result_file = "{}_a-{}{}".format(results_name, a, file_ending)
print(result_file)

# f-strings are assigned by adding the character f before the string
# These are useful for having a good idea about what you're printing
result_file = f"{results_name}_a-{a}{file_ending}"
print(result_file)

# formatting strings is useful when working with or saving multiple files.
# Here we can use some info to give file names to our images.
image_filename = f"{results_name}_a-{a}.jpg"


### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# The list is defined using square brackets
ucs_list = [86.2, 78.1, 55.3]

# You may access the values of the list (indexing the list) a list by using 
# integers in square brackets directly following the variable name of the list
# Indexing starts at 0, (i.e. the first entry is at index 0, the second at index 1, etc.)
ucs_list[0]  # returns the first element
ucs_list[1]  # returns the second element
ucs_list[-1]  # returns the last element

# You may add data to the list by using the .append() function
ucs_list.append(67.9)

# You can find the amount of entries of a list using len()
len(ucs_list)
# returns: 4

# You can slice a list by using colons, it returns a list
# from (and including) the index 0 to, but not including index 2
ucs_list[0:2]
# returns: [86.2, 78.1]

# You may assign a new value to an entry of the list by using the index
ucs_list[0] = 90.0
# The first entry of the list is now 90.0 instead of 86.2

# Tuples act similarly to lists in many ways, but cannot change
# after assignment. Tuples are defined by using regular parentheses
ucs_tuple = (86.2, 78.1, 55.3)

# since the tuple cannot be changed, the following line would throw an error
# ucs_tuple.append(78)


# Dictionaries store data in an unstructured way
# These are indexed using keys (strings)

# Dictionaries are defined by using curly brackets
# Key and value pairs are separated by colon, entries
# are separated with a comma. The values can be any data type

book_authors = {"harry potter": "J.K. Rowling",
                "lord of the rings": "J.R.R Tolkien",
                "intro to statistics": ["John Doe", "Jane Doe"]}


# We can use the value of a dictionary item by indexing it with the key

ucs_dict = {
    "granite": [90, 90, 91],
    "limestone": [78, 87, 89]
}

# Lets try to append a value to the list of UCS values for limestone
ucs_dict["limestone"].append(88)

# We can now look at the final value of the list of UCS values for limestone
# by indexing the dictionary with the key "limestone" and the list with -1
ucs_dict["limestone"][-1]
# returns: 88

# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1
list(range(3, 10))

# you can set the starting number and the step size similarly
# to how we slice lists (start, stop, step)
list(range(3, 10, 2))


# Code suggestions for Exercise 3 and 4 will be added after the next session
