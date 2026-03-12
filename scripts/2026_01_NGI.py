"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in March
2026 in 4x4 hour sessions.

This script contains the code that was written during the first session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 1 on 11th of March 2026
###########################


### introduction and overview over uv and VS Code

""" Terminal

Create uv environment:
uv init --no-readme

Adding ipykernel to environment:
uv add ipykernel

Activate environment:
.venv\Scripts\activate

"""


### basic datatypes: strings, integers, floats, print function

# Datatypes

# integer numbers are represented with an "int" data type
1

20

# decimal numbers are represented with a "float" data type

1.2

2.5

# text is represented with a "str" data type
# "str" is short for string, or string of characters
# you may use either double quotes, ", single quotes, ', or
# tripled double or single quotes, """ / ''', to construct
# a string

"This is a double quote string"
'This is a single quote string'

"That's it, here we can use the apostrophe"

# You may use triple quotes to write long strings over multiple lines
"""
String
Covering
Many
Lines
"""

# You can print the data to the console by using the print() function
print("Hello World!")


# You may check the datatype by using the type() function, if you want
# to see the results, you have to print it out

print(type(2.0))
# returns: float

# you can change the data type by using the int(), float() and str()
# functions. Data might get lost in the process

print(int("1"))
# returns: 1

print(float("1.2"))
# returns: 1.2

print(str(1.2))
# returns: "1.2"

# Exercise 1

print("Hello World!")


### operators: +, -, /, *, **, //, %
print(1 + 1)  # addition
print(3 - 5)  # subtraction
print(12 / 3)  # division
print(2 * 4)  # multiplication
print(2**4)  # to the power of
print(13 // 4)  # floored division / integer division
print(11 % 3)  # modulo / remainder

# Note that the + operator works differently for strings and numbers
print("1"+"1")
# returns '11', a string

print(1+1)
# returns 2, an integer


# Exercise 2
print(5**8)       # 5 to the power of 8
print(9**0.5)     # square root of 9
print(14 % 5)     # remainder of 14 divided by 5
print((13//3)*3)  # the product of the floored division of 13 by 3 and 3

print()

### variables, string formatting

# Variables can be assigned data by setting them equal to a value
# python automatically assigns a data type to the variable

variable = 1

print(type(variable))

variable = "john"

print(type(variable))


# You may also assign multiple variables respectively using comma. The code
# below assigns the value of 1 to variable a and the value of 2 to variable b

variable_1, variable_2 = 1, "Library"

# This is the same as:
variable_1 = 1
variable_2 = "Library"


# variable names should be explicit and informative

dist_watertower_road_m = 987  # Informative variable name, with unit
b = 1234                      # Not informative, we don't know what this variable is for



# These variables will be used in the following examples

rock_type = "limestone"
rock_ucs_MPa = 90


# There are multiple ways to format a string

# string concatenation: "string" + "another string"
text = "The UCS of the " + rock_type + " is " + str(rock_ucs_MPa) + "MPa"
print(text)

# .format() function replaces the {} with the function inputs
# The string may be stored as a variable. We can add multiple inputs
# to .format()
text = "The UCS of the {} is {}MPa".format(rock_type, rock_ucs_MPa)
print(text)

# f-strings are assigned by adding the character f before the string
# These are useful for having a good idea about what you're printing
text = f"The UCS of the {rock_type} is {rock_ucs_MPa}MPa"
print(text)

# formatting strings is useful when working with or saving multiple files.
# Here we can use some info to give file names to our images.
test_type = "UCS"
rock_type = "limestone"
file_name = f"{test_type}_{rock_type}.png"

### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# The list is defined using square brackets

my_list = [1, 2, 3]
print(my_list)

# You may access the values of the list (indexing the list) a list by using
# integers in square brackets directly following the variable name of the list
# Indexing starts at 0, (i.e. the first entry is at index 0, the second at index 1, etc.)

first_entry = my_list[0]
print(first_entry)

second_entry = my_list[1]
print(second_entry)

last_entry = my_list[-1]
print(last_entry)

# You may add data to the list by using the .append() function

my_list.append(4)
print(my_list)

# You can find the amount of entries of a list using len()
print(len(my_list))

# You can slice a list by using colons, it returns a list
# from (and including) the index 0 to, but not including
# index 2

print(my_list[1:3])

# You may assign a new value to an entry of the list by using the index

my_list[2] = 6
print(my_list)

# Tuples act similarly to lists in many ways, but cannot change
# after assignment. Tuples are defined by using regular parentheses

my_tuple = (1, 2, 3)
print(my_tuple)

print(my_tuple[1])

# since the tuple cannot be changed, the following line would throw an error
# ucs_tuple.append(78)

# my_tuple.append(4)
# my_tuple[2] = 6
print()

# Dictionaries store data in an unstructured way
# These are indexed using keys (strings)

# Dictionaries are defined by using curly brackets
# Key and value pairs are separated by colon, entries
# are separated with a comma. The values can be any data type

rock_dict = {"limestone": 90, "sandstone": [85, 89], "chalk": 20}

# The values of a dictionary do not need to be strings
# they can be any data type, like lists

# We can use the value of a dictionary item by indexing it with the key
print(rock_dict["sandstone"])

# Lets try to append a value to the list of UCS values for sandstone
rock_dict["sandstone"].append(70)

# We can now look at the final value of the list of UCS values for sandstone
# by indexing the dictionary with the key "sandstone" and the list with -1
print(rock_dict["sandstone"][-1])


# Exercise 3

# It's normal practice to start with an empty list and append values to it
char_list = []

# We can use the len() function to find the length of a string
# and append it to the list
char_list.append(len("marl"))
char_list.append(len("gneiss"))
char_list.append(len("limestone"))
char_list.append(len("eclogite"))

print(char_list)

# Here I use the sum() function to sum the last three entries of the list
result = sum(char_list[-3:])

# Alternatively, we could sum the last three entries of the list by using the + operator
result = char_list[-3] + char_list[-2] + char_list[-1]

# Here we print the result by formatting a string in two different ways
print("the result is: {}".format(result))
print(f"the result is: {result}")


# Exercise 4

rock_list = ['gneiss', 'marl', 'limestone']
rock_tuple = ('gneiss', 'marl', 'limestone')

# First we print the first two entries of the list and tuple
print(rock_list[:2])
print(rock_tuple[:2])

# We try to append a new entry to the list and tuple
# This will work for the list, but throw an error for the tuple
rock_list.append('greenschist')
# rock_tuple.append('greenschist')

# Now we try to change the second entry of the list and tuple
# This will work for the list, but throw an error for the tuple
rock_list[1] = 'dolomite'
# rock_tuple[1] = 'dolomite'
