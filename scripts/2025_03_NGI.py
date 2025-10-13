"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in October
2025 in 4x4 hour sessions.

This script contains the code that was written during the third session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 3 on 13th of October 2025
###########################

# Exercise 3 - bonus

# Starting by defining the list of rocks and an empty list to hold the
# character counts
rocks = ["marl", "gneiss", "limestone", "eclogite"]
char_counts = []

# Looping through the rock list and appending the character count (len()) of
# each rock to the char_counts list
for rock in rocks:
    char_counts.append(len(rock))

print(char_counts)

# Summing the last three entries in the char_counts list
# by indexing from the third last entry (index -3) to the end of the list
last_three_sum = sum(char_counts[-3:])

# Printing the result using different methods
print("the result is: {}".format(last_three_sum))
print(f"the result is: {last_three_sum}")


# Exercise 8

# First we define the two lists
rock_list = ["gneiss", "marl", "limestone"]
ucs_list = [150, 45, 90]

# I create an empty dictionary to fill later
rock_dict = {}

# Now we loop through the rock list and assign the UCS values
# to the corresponding rock type by using the rock name
# as the key and assigning it the UCS value from the ucs_list
for i, rock in enumerate(rock_list):
    rock_dict[rock] = ucs_list[i]

# Alternative way using dictionary comprehension and the zip() function
rock_dict = {rock: ucs for rock, ucs in zip(rock_list, ucs_list)}

# Here we add a new entry to the dictionary
rock_dict["sandstone"] = 70

# I loop through the dictionary keys and print the rock with
# its corresponding UCS value
for rock in rock_dict.keys():
    ucs = rock_dict[rock]
    print(f"The {rock} has a UCS of {ucs} MPa")

# Alternative way using the items() method to get both key and value
for rock, ucs in rock_dict.items():
    print(f"The {rock} has a UCS of {ucs} MPa")


# Exercise 9

# We have the following list of values
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# Mean
mean = sum(c) / len(c)

# Rounding is saved for the printing step to keep the full precision
# in our variables
print(f"mean value: {round(mean, 2)}")

# Median
sorted_c = sorted(c)

# For the median we need to check if the number of elements is even or odd
# If even, we take the average of the two middle elements
# If odd, we take the middle element

# even
if len(sorted_c) % 2 == 0:

    # We can find the upper of the two middle indices by integer division
    # of the length of the list by 2
    high_middle_index = len(sorted_c) // 2

    # The lower middle index is one less than the upper middle index
    low_middle_index = high_middle_index - 1

    # The median is the mean of the two middle values
    median = (sorted_c[low_middle_index] + sorted_c[high_middle_index]) / 2

# odd
else:
    # First we find the middle index by integer division of the length
    middle_index = len(sorted_c) // 2

    # The median is the value at the middle index
    median = sorted_c[middle_index]

print(f"median value: {round(median, 2)}")

# Variance

# We first make an empty list for the squared differences
squared_difference_list = []

# Now we loop through the original list, subtract the mean and square
# the result, appending it to the squared_difference_list
for c_i in c:
    squared_difference_list.append((c_i - mean) ** 2)

# The variance is the mean of the squared differences
variance = sum(squared_difference_list) / len(c)

print(f"variance: {round(variance, 2)}")

# standard deviation

# We compute the standard deviation as simply the square root of the variance
std = variance**0.5

print(f"standard deviation: {round(std, 2)}")


### functions

# Functions may be used to carry out a block of code whenever called. A function
# is defined by using the def keyword followed by the function name with the input
# argument(s) assigned inside the parenthesis. The value returned from the function
# is defined using the return keyword

my_number = 10


def my_function(a, b):
    """
    Adds together two inputs.
    """  # This is a docstring, which describes what the function does
    result = a + b
    return result


# We can call the function by using its name and passing the required inputs
my_result = my_function(my_number, 2)


# It is useful to assign data types to the inputs, which is done by separating
# the input argument name and it's corresponding data type by colon in the
# function definition. The data type of the return value is given after the ->
# symbol.


def my_function(a: int, b: int) -> int:
    result = a + b
    return result


# If we try to pass inputs of the wrong data type, this will not cause an error.
# The type hints are not enforced, but they are useful for documentation and
# will be picked up by code editors to warn you if you try to pass the wrong type
my_result = my_function(str(1), str(2))

print(my_result)
# This will print "12" as the function concatenates the two strings


# We can set default values to inputs by specifying them after the equals sign
# in the function definition.


def my_function(a, b=2):
    result = a + b
    return result


# We can also do this with type hints
def my_function(a: int, b: int = 2) -> int:
    result = a + b
    return result


# Setting default values means that we do not need to pass all the inputs to
# the function.
my_result = my_function(3)

print(my_result)
# This will print 5, as the default value of b=2 is used


# Exercise 10


# We can define functions for the calculations we did in Exercise 9
# Here I include some docstrings to describe what each function does
def mean_fn(input_list: list) -> float:
    """computes the arithmetic mean of an input list"""
    mean = sum(input_list) / len(input_list)
    return mean


def median_fn(input_list: list) -> float | int:
    """computes the median of an input list

    if the list has even numbered elements, the median
    is computed as the mean of the two middle values"""
    sorted_list = sorted(input_list)

    # even
    if len(sorted_list) % 2 == 0:
        high_middle_index = len(sorted_list) // 2
        low_middle_index = high_middle_index - 1
        median = (sorted_list[low_middle_index] + sorted_list[high_middle_index]) / 2

    else:  # odd
        middle_index = len(sorted_list) // 2
        median = sorted_list[middle_index]

    return median


# Inside the variance function we can call the mean function
# as we need to compute the mean of the squared differences
# this shows how functions can be built on top of each other
def variance_fn(input_list: list) -> float:
    """computes the variance of an input list"""
    mean = mean_fn(input_list)
    squared_difference_list = [(x - mean) ** 2 for x in input_list]

    variance = mean_fn(squared_difference_list)
    return variance


def std_fn(input_list: list) -> float:
    """computes the standard deviation of an input list"""
    variance = variance_fn(input_list)
    std = variance**0.5
    return std


# Now we can call the functions on our list c
mean = mean_fn(c)
median = median_fn(c)
var = variance_fn(c)
std = std_fn(c)

# And print the results
print(f"mean value: {round(mean, 2)}")
print(f"median value: {round(median, 2)}")
print(f"variance: {round(var, 2)}")
print(f"standard deviation: {round(std, 2)}")
