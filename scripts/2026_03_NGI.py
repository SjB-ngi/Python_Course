"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in March
2026 in 4x4 hour sessions.

This script contains the code that was written during the third session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 3 on 25th of March 2026
###########################

# Recap of session 2

# Zip function
from tornado.concurrent import future_set_exception_unless_cancelled
rocks = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff', 'quartzite',
         'kaolin', 'phonolite', 'gneiss', 'sand', 'diabase', 'black coal',
         'slate', 'andesite', 'andesite', 'gypsum and anhydrite', 'greywacke',
         'suevite']

years = list(range(2007, 2007+len(rocks)))

# You can print this using the iterator, i, and indexing the lists
for i in range(len(rocks)):
    print(f'{years[i]}: {rocks[i]}')

# Or you can iterate over each paired up list element with zip()
for rock, year in zip(rocks, years):
    print(f"{year}: {rock}")


ucs_values = [200, 150, 300, 60, 80, 250, 20, 180, 250, 30, 250, 15, 150, 200,
                         200, 40, 160, 70]

# We can zip together as many items as we want, it doesn't have to be two
for rock, year, ucs in zip(rocks, years, ucs_values):
    print(f"{year}: {rock} with ucs of {ucs}")

# Exercise 3 - bonus

rocks = ["marl", "gneiss", "limestone", "eclogite"]
char_list = []

for rock in rocks:
    # Appending the length of the list item value
    char_list.append(len(rock))

for i in range(len(rocks)):
    char_list.append(len(rocks[i]))

# This list now has the values of each the lengths
print(char_list)

last_three_sum = sum(char_list[-3:])

print("the result is: {}".format(last_three_sum))
print(f"the result is: {last_three_sum}")

# Exercise 8

rock_list = ["gneiss", "marl", "limestone"]

ucs_list = [150, 45, 90]

rock_dict =  {}

for rock, ucs in zip(rock_list, ucs_list):
    rock_dict[rock] = ucs

rock_dict["granite"] = 200

for rock in rock_dict.keys():
    print(f"The {rock} has a UCS of {rock_dict[rock]} MPa")


# Exercise 9
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]
c_sorted = sorted(c)

mean = sum(c)/len(c)

if len(c)%2 != 0:
    median = c_sorted[len(c)//2]
else:
    median = (c_sorted[len(c)//2 - 1] + c_sorted[len(c)//2]) / 2

squared_differences = [(c_i-mean)**2 for c_i in c]
var = sum(squared_differences)/len(squared_differences)

std = var**0.5

print("mean value:", round(mean, 2))
print("median value:", round(median, 2))
print("variance:", round(var, 2))
print("standard deviation:", round(std, 2))

### functions

# Functions may be used to carry out a block of code whenever called. A function
# is defined by using the def keyword followed by the function name with the input
# argument(s) assigned inside the parenthesis. The value returned from the function
# is defined using the return keyword

my_number = 45

def add_two(x):
    new_x = x + 2
    return new_x

print(add_two(my_number))

# It is useful to assign data types to the inputs, which is done by separating
# the input argument name and it's corresponding data type by colon in the
# function definition. The data type of the return value is given after the ->
# symbol.

def add(x: int, y: int) -> int:
    new_value = x + y
    return new_value

print(add(1, 2))

# We can set default values to inputs by specifying them after the equals sign
# in the function definition.

def add(x, y=2):
    new_value = x + y
    return new_value

add(1)

# Setting default values means that we do not need to pass all the inputs to
# the function.

# Exercise 10

def mean_fn(number_list: list) -> float:
    """
    computes the mean of a list of numbers

    Parameters
    ---------------
    number_list: list
        A list of numbers

    Returns
    ---------------
    mean: float
        the mean of the number list
    """
    mean = sum(number_list)/len(number_list)
    return mean

def median_fn(number_list: list) -> float:
    """
    Computes the median of a list of numbers. If the list is even,
    the mean of the two middle values is returned
    
    Parameters
    ---------------
    number_list: list
        A list of numbers

    Returns
    ---------------
    median: float
        the median of the number list
    
    """
    number_list_sorted = sorted(number_list)
    if len(c)%2 != 0:
        median = number_list_sorted[len(c)//2]
    else:
        median = (number_list_sorted[len(c)//2 - 1] + number_list_sorted[len(c)//2]) / 2
    return median

def variance_fn(number_list):
    number_mean = mean_fn(number_list)
    squared_differences = [(c_i-number_mean)**2 for c_i in c]
    var = mean_fn(squared_differences)
    return var

def std_fn(number_list):
    var = variance_fn(number_list)
    std = var**0.5
    return std

print("mean value:", round(mean_fn(c), 2))
print("median value:", round(median_fn(c), 2))
print("variance:", round(variance_fn(c), 2))
print("standard deviation:", round(std_fn(c), 2))


# There are multiple ways to import functions from another script
# NOTE: The script must be in the same folder as the script you're using

# We can import functions directly

from python_course_utility import custom_median

# This lets us use the function directly
print(custom_median(c))

# Multiple functions can be imported at once by separating them with a comma

from python_course_utility import custom_median, custom_mean

print(custom_median(c))

# We can also import all functions from a script using the asterisk, *

from python_course_utility import *

print(custom_std(c))

# If we want to import all functions from a script, we can also import the
# script itself

import python_course_utility

print(python_course_utility.custom_median(c))

# To make the code more readable, we can import the script with an abbreviated
# name. This is done by using the "as" keyword

import python_course_utility as pcu

print(pcu.custom_median(c))

"""
To install the groundhog package, which contains functions for geotechnical engineering,
we use the following command in the terminal:

uv add groundhog
"""

# Now we can import functions from the groundhog package
from groundhog.deepfoundations.axialcapacity.endbearing import unitendbearing_clay_almhamre