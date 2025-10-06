"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in October
2025 in 4x4 hour sessions.

This script contains the code that was written during the second session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 2 on 8th of November 2025
###########################


### Boolean operators: or, and, not
# These are used to do operations on True/False data, i.e boolean data


# "not" is used to reverse a boolean value

# "or" is used to check if at least one of the two boolean values is True

# "and" is used to check if both boolean values are True


# comparison operators: <, >, <=, >=, ==, !=
# These are used to compare two values, and return a boolean value


### control structures: conditional statements: if, elif, else, match cases

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False


# The code in the indentation block below will only run if the condition is True


# elif can be used for additional tests NB! only if the first if statement
# is false


# match-cases are a new alternative to check if a variables matches something (==)


### control structures: loops: while loop, for loop
# loops are used to repeat parts of code

# while loop is a loop that runs until a condition is not True anymore


# Exercise 5


# a while loop can be used to iterate over a list

# The following two lists have items such that the indices match


# We create an empty list to store the results


# create the i variable to use for iterating over the indices of the lists


# a better solution is however to use a for loop which is always finite


# We create an empty list to store the results

# for i in range(len(...)): is a typical construction to get an index


# Instead of iterating through indices, we may also iterate through
# the list elements


# The enumerate() function can be used to get both an element and the index


# zip will match the elements of two lists together by their indices
# and return a list of tuples which we can iterate over


# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop


# it is short but comes at the price of readability


# Exercise 6


# Exercise 7
