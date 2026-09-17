"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in September
2026 in 4x4 hour sessions.

This script contains the code that was written during the second session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 2 on 17th of September 2026
###########################

### control structures: loops: while loop, for loop
# loops are used to repeat parts of code


# The following two lists have items such that the indices match
rocks =         ["granite", "limestone",    "sandstone" ]
ucs_values =    [90,        80,             87          ]


# A for loop lets us iterate through items in a sequence

# for i in range(len(...)): is a typical construction to get an index


# Instead of iterating through indices, we may also iterate through
# the list elements directly


# The enumerate() function can be used to get both an element and the index


# zip will match the elements of two lists together by their indices
# and return a list of tuples which we can iterate over


# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop


# Exercise 5


# Exercise 6

rocks = [
    "granite",
    "sandstone",
    "basalt",
    "limestone",
    "tuff",
    "quartzite",
    "kaolin",
    "phonolite",
    "gneiss",
    "sand",
    "diabase",
    "black coal",
    "slate",
    "andesite",
    "andesite",
    "gypsum and anhydrite",
    "greywacke",
    "suevite",
]


# Exercise 3 - using loops


# Exercise 7


# Exercise 8


### functions

# Functions may be used to carry out a block of code whenever called. A function
# is defined by using the def keyword followed by the function name with the input
# argument(s) assigned inside the parenthesis. The value returned from the function
# is defined using the return keyword


# It is useful to assign data types to the inputs, which is done by separating
# the input argument name and it's corresponding data type by colon in the
# function definition. The data type of the return value is given after the ->
# symbol.


# If we try to pass inputs of the wrong data type, this will not cause an error.
# The type hints are not enforced, but they are useful for documentation and
# will be picked up by code editors to warn you if you try to pass the wrong type


# We can set default values to inputs by specifying them after the equals sign
# in the function definition.


# Setting default values means that we do not need to pass all the inputs to
# the function.


# Exercise 9


# Optional lecture on classes
