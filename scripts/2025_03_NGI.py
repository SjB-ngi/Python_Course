# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics"
from the Norwegian Geotechnical Institute. The course is held in May 2025 in 4x4 hour sessions.

This script contains the code that was written during the third session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""


###########################
# session 3 on 12th of May 2025
###########################

# Exercise 3 - bonus

# First we create an empty list to hold the character counts
rock_name_character_counts = []

# We iterate through the list and add the amount of characters to the empty list
rock_names = ["marl", "gneiss", "limestone", "eclogite"]
for rock_name in rock_names:
    rock_name_character_counts.append(len(rock_name))

# We print the list to the console
print(rock_name_character_counts)

# We calculate the total amount of characters for the last three entries
last_three_elements_sum = sum(rock_name_character_counts[-3:])

# We print it to the console using format in two different ways
print("the result is: {}".format(last_three_elements_sum))
print(f"the result is: {last_three_elements_sum}")


# Exercise 8

# We create the two lists we have been given
rock_list = ['gneiss', 'marl', 'limestone']
ucs = [150, 45, 90]

# We create the empty dictionary to hold the data
rock_dict = {}

# We use zip to pair up the data, and dict to turn it into a dictionary
# There are other perfectly valid ways to do this as well!
for rock, ucs_value in zip(rock_list, ucs):
    rock_dict[rock] = ucs_value

# We add a new entry to the dictionary
rock_dict["sandstone"] = 120

# We iterate through the keys of the dictionary and print a formatted
# string for each case.
for rock in rock_dict.keys():
    print(f"The {rock} has a UCS of {rock_dict[rock]} MPa")

# Alternative using .items()
for rock, rock_ucs in rock_dict.items():
    print(f"The {rock} has a UCS of {rock_dict[rock]} MPa")



# Exercise 9

# We create the list of numbers we have been given
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# We precompute the number of items in the list
# This is a good practice, as it avoids having to call len() multiple times
n_items = len(c)

# Mean
mean = sum(c)/n_items

# Median

# We make a sorted version of the list
c_sorted = sorted(c)

# If the amount of items is even, we need to calculate the mean of the two
# middle values.
if len(c) % 2 == 0:

    # We find the indices of the two middle values
    # The upper middle index is the integer division of the size of the list
    # by 2, the lower middle index is one less than that

    upper_middle_index = n_items//2  # upper middle value, because indices start at 0
    lower_middle_index = upper_middle_index - 1

    # We retrieve the two middle values from the sorted list and calculate
    # the mean of them
    median = (c_sorted[lower_middle_index] + c_sorted[upper_middle_index])/2

# If the amount of items is odd, we take the middle value by using the integer
# division of the size of the list by 2
else:
    # Find the index of the middle value
    middle_index = n_items//2

    # We retrieve the middle value from the sorted list
    median = c_sorted[middle_index]

# Variance

# First I'm going to create an empty list to hold the squared differences
squared_differences = []
for c_i in c:   # I use c_i as the iterator variable, indicating that we are 
                # iterating through the list c

    # We calculate the squared difference between the current value and the mean
    # and append it to the list
    squared_difference = (c_i - mean)**2
    squared_differences.append(squared_difference)

# We calculate the variance by computing the mean of the squared differences
variance = sum(squared_differences)/n_items


# Standard deviation

# The standard deviation is the square root of the variance
# We can use the exponentiation operator ** to calculate the square root
# with the exponent 0.5
standard_deviation = variance**0.5

# Print results

# Here I'm rounding the values to 2 decimal places inside the print statement
# using the round() function. The round() function takes two arguments, the
# number to round and the number of decimal places to round to.
print(f"mean value: {round(mean, 2)}")
print(f"median value: {round(median, 2)}")
print(f"variance: {round(variance, 2)}")
print(f"standard deviation: {round(standard_deviation)}")

### functions

# Functions may be used to carry out a block of code whenever called. A function
# is defined by using the def keyword followed by the function name with the input
# argument(s) assigned inside the parenthesis. The value returned from the function
# is defined using the return keyword


def simple_addition(a_value, b_value):
    simple_sum = a_value + b_value
    return simple_sum


a = 20
b = 30.0

ss = simple_addition(a, b)
ss = simple_addition(a_value=a, b_value=b)

print(f"The result of the sum is {ss}")


# It is useful to assign data types to the inputs, which is done by separating
# the input argument name and it's corresponding data type by colon in the 
# function definition. The data type of the return value is given after the ->
# symbol.

def simple_addition(a_value: int, b_value: float = 30.0):
    simple_sum = a_value + b_value
    return simple_sum

print(simple_addition(1, 1))

# We can set default values to inputs by specifying them after the equals sign
# in the function definition.


def simple_addition(a_value, b_value=30.0):
    simple_sum = a_value + b_value
    return simple_sum


# Setting default values means that we do not need to pass all the inputs to 
# the function.

a = simple_addition(1)  # b_value is set to the value of 30.0
print(f"The result of the sum is {a}")



# Exercise 10

# We want to refactor the code we wrote in exercise 9 into functions


def custom_mean(c: list) -> float:
    return sum(c)/len(c)


def custom_median(c: list) -> float:
    # We make a sorted version of the list, this is done in a new variable
    # inside the function, as we will likely not need the sorted list later
    c_sorted = sorted(c)

    # Even number of items
    if len(c) % 2 == 0:

        # We find the indices of the two middle values
        upper_middle_index = len(c)//2  # upper middle value, because indices start at 0
        lower_middle_index = upper_middle_index - 1

        # We calculate the mean of the two middle values
        median = (c_sorted[lower_middle_index] + c_sorted[upper_middle_index])/2

    # Odd number of items
    else:
        # Find the index of the middle value
        middle_index = len(c)//2

        # We retrieve the middle value from the sorted list
        median = c_sorted[middle_index]

    return median


def custom_variance(c: list) -> float:
    # Use the mean function to compute the mean
    mean = custom_mean(c)

    # Instantiate a temporary list
    squared_differences = []

    # Append the squared differences to the list
    for c_i in c:
        squared_differences.append((c_i - mean)**2)

    # Computing variance as the mean of the squared differences
    # Here we could also use the custom_mean() function if we want
    variance = 1/len(c) * sum(squared_differences)

    return variance


def custom_std(c: list) -> float:
    variance = custom_variance(c)
    return variance**(1/2)


def statistical_params(c: list) -> tuple:
    """
    This function calculates the mean, median, variance and standard deviation
    of a list of numbers. It returns the values as a tuple.

    Parameters
    ----------
    c : list
        A list of numbers.

    Returns
    -------
    mean : float
        The mean of the numbers in the list.
    median : float
        The median of the numbers in the list.
    variance : float
        The variance of the numbers in the list.
    std : float
        The standard deviation of the numbers in the list.
    """
    mean = custom_mean(c)
    median = custom_median(c)
    variance = custom_variance(c)
    std = custom_std(c)

    return mean, median, variance, std


# With all the functions defined, we can group the operations like this:
mean = custom_mean(c)
median = custom_median(c)
variance = custom_variance(c)
std = custom_std(c)

# Now we print all the values rounded to 2 decimals, which we can do inside
# the print statement
print(f"mean value: {round(mean, 2)}")
print(f"median value: {round(median, 2)}")
print(f"variance: {round(variance, 2)}")
print(f"standard deviation: {round(std, 2)}")

