"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in September
2026 in 4x4 hour sessions.

This script contains the code that was written during the second session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Modifications: Sjur Beyer, sjur.beyer@ngi.no
Author: Dr. Georg H. Erharter
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
for i in range(len(rocks)):
    print(f"The UCS of {rocks[i]} is {ucs_values[i]}")

print()
# Instead of iterating through indices, we may also iterate through
# the list elements directly
for rock in rocks:
    print(rock)

print()
# The enumerate() function can be used to get both an element and the index
for i, rock in enumerate(rocks):
    print(f"The UCS of {rock} is {ucs_values[i]}")

# zip will match the elements of two lists together by their indices
# and return a list of tuples which we can iterate over
for rock, ucs in zip(rocks, ucs_values):
    print(f"The UCS of {rock} is {ucs}")

# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop
[print(rock) for rock in rocks]

# Exercise 5

factors_list = []

for number in range(1, 1000):
    if not number % 5 or not number % 3:
        factors_list.append(number)

print(sum(factors_list))

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

start_year = 2007

for i in range(len(rocks)):
    current_year = start_year + i
    print(f"The rock of the year {current_year} is {rocks[i]}")


print()

# Exercise 7
rock_list = ["gneiss", "marl", "limestone"]
ucs = [150, 45, 90]

rock_dict = {}

for i, rock in enumerate(rock_list):
    rock_dict[rock] = ucs[i]

rock_dict["granite"] = 90

for rock in rock_dict:
    print(f"The {rock} has a UCS of {rock_dict[rock]}")

rock_list = list(rock_dict.keys())

print(rock_list)

# Exercise 8
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# Mean
mean_c = sum(c)/len(c)

# Variance
squared_differences_c = []

for c_i in c:
    squared_differences_c.append((c_i-mean_c)**2)

variance_c = sum(squared_differences_c)/len(squared_differences_c)

# Standard deviation
standard_deviation_c = variance_c**0.5

# Printing results
print(f"mean value: {round(mean_c, 2)}")
print(f"variance: {round(variance_c, 2)}")
print(f"standard deviation: {round(standard_deviation_c, 2)}")


### functions

# Functions may be used to carry out a block of code whenever called. A function
# is defined by using the def keyword followed by the function name with the input
# argument(s) assigned inside the parenthesis. The value returned from the function
# is defined using the return keyword

def function(x):
    new_number = x + 2
    return new_number

print(function(2))


# It is useful to assign data types to the inputs, which is done by separating
# the input argument name and it's corresponding data type by colon in the
# function definition. The data type of the return value is given after the ->
# symbol.

def function(x: int, y: float) -> int:
    new_number = x + 2
    another_number = y - 3
    return new_number

print(function(2, 3))

# If we try to pass inputs of the wrong data type, this will not cause an error.
# The type hints are not enforced, but they are useful for documentation and
# will be picked up by code editors to warn you if you try to pass the wrong type


# We can set default values to inputs by specifying them after the equals sign
# in the function definition.

def calculate_qt(qc, u2, a=0.8, t="SCPT"):
    """
    Calculates corrected tip resistance
    a = 0.8
    """
    return qc+u2*(1-a)

print(calculate_qt(20, 10))

# Setting default values means that we do not need to pass all the inputs to
# the function.

# Exercise 9

def mean(x: list) -> float:
    return sum(x)/len(x)

def variance(x: list) -> float:

    mean_x = mean(x)
    squared_differences = []
    for x_i in x:
        squared_differences.append((x_i-mean_x)**2)
    return mean(squared_differences)

def std_dev(x: list) -> float:
    var = variance(x)
    return var**0.5

# Printing
print(f"mean value: {round(mean(c), 2)}")
print(f"variance: {round(variance(c))}")
print(f"standard deviation: {round(std_dev(c))}")

# Optional lecture on classes
