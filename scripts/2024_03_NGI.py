# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics (Pilot course)"
from the Norwegian Geotechnical Institute. The course is held in November to
December 2024 in 4x4 hour sessions.

This script contains the code that was written during the third session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""


###########################
# session 3 on 2nd of December 2024
###########################

# repetition


# Exercise 3 - bonus

rock_names = ["marl", "gneiss", "limestone", "eclogite"]
rock_name_character_counts = []     # we instantiate an empty list to hold the
                                    # character counts

# We iterate through the list and add the amount of characters to the empty list
for rock_name in rock_names:
    rock_name_character_counts.append(len(rock_name))

print(rock_name_character_counts)

# We calculate the total amount of characters for the last three entries
last_three_elements_sum = sum(rock_name_character_counts[-3:])

# We print it to the console using format in two different ways
print("the result is: {}".format(last_three_elements_sum))
print(f"the result is: {last_three_elements_sum}")



# Exercise 8

rock_list = ["gneiss", "marl", "limestone"]
ucs = [150, 45, 90]

# We use zip to pair up the data, and dict to turn it into a dictionary
rock_dict = dict(zip(rock_list, ucs))

# We add a new entry to the dictionary
rock_dict["sandstone"] = 90

# We iterate through the keys of the dictionary and print a formatted
# string for each case.
for rock in rock_dict.keys():
    print(f"The {rock} has a UCS of {rock_dict[rock]} MPa")

# Alternative using .items()
for rock, rock_ucs in rock_dict.items():
    print(f"The {rock} has a UCS of {rock_ucs} MPa")



# Exercise 9
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# We use sum() to sum up the numbers and len() to count up the numbers, after
# we compute the mean.
mean = sum(c) / len(c)

# We use round() to round the number to a specified amount of decimals
mean = round(mean, 2)

# We print the value to the console
print(f"mean value: {mean}")

# For the median we need a sorted list, so we use the sorted() function
c_sorted = sorted(c)

# Medians are computed differently for even and odd entry lists, first we check
# if the amount of entries is even, else it will be odd
if len(c) % 2 == 0:
    
    # We use the integer division of the size of the list to find indices
    # in the middle of the sorted list
    upper_val = c_sorted[len(c_sorted)//2]      # upper middle value
    lower_val = c_sorted[len(c_sorted)//2-1]    # subtract one from the index
                                                # to get the lower middle value
    
    median = (upper_val + lower_val)/2

else:  # Odd case
    # We retrieve the value in the middle of the list like the lower value above
    median = c_sorted[len(c_sorted)//2-1]

median = round(median, 2)
print(f"median value: {median}")


# For variance we make a temporary list to store the squared differences
variance_temp = []

# We iterate through all the data points and append the squared differences
# to the empty list
for c_i in c:
    variance_temp.append((c_i-mean)**2)

# We compute the variance by computing the mean of the squared differences
variance = 1/len(c) * sum(variance_temp)

variance = round(variance, 2)
print(f"variance: {variance}")

# With the variance we can compute the standard deviation by taking the root
# of the variance, which we can do by raising to the power of 1/2
std = variance**(1/2)

std = round(std, 2)
print(f"standard deviation: {std}")


### functions

# Functions may be used to carry out a block of code whenever called. A function
# is defined by using the def keyword followed by the function name with the input
# argument(s) assigned inside the parenthesis. The value returned from the function
# is defined using the return keyword

def function(x, y):
    # The code inside the indented block underneath def is ran when a function
    # is called

    print(x)  # in this case the value in the first argument is printed
    
    return x+y  # The function outputs the result of x + y

function(1, 2)
# prints: 1
# returns: 3

a = function(1, 2)
# prints: 1
# the value of a is set to be 3

# It is useful to assign data types to the inputs, which is done by separating
# the input argument name and it's corresponding data type by colon in the 
# function definition. The data type of the return value is given after the ->
# symbol.
def function(x: int, y: int) -> int:
    print(x)
    
    # The data types are only indicative, if we want to force this, we could
    # use some logic inside the function which will not allow the function
    # to run unless the input 
    if not isinstance(x, int) or isinstance(y, int):
        raise ValueError("instance of x must be an integer")    # raise is used
                                                                # to cause an
                                                                # error
    
    return x + y

# We can set default values to inputs by specifying them after the equals sign
# in the function definition, which is done below for y.
def function(x: int, y: int=2):
    if not isinstance(x, int) or isinstance(y, int):
        raise ValueError("instance of x must be an integer")
    return x+y

# Setting default values means that we do not need to pass all the inputs to 
# the function. Below, the function is evaluated on the number 3, and y is set
# to the value of 2.
a = function(3)
# the value of a is set to be 5

print(a)



# Exercise 10

# We define a custom mean function by using def and specifying the input as 
# a list, the mean is computed as above.
def custom_mean(input_list: list) -> float:
    return sum(input_list) / len(input_list)

# We define the custom median function in the same way as the custom mean
# function above. Here it is important that we handle both odd and even length
# lists since we may want to use this on either in the future.
def custom_median(input_list: list) -> float:
    input_sorted = sorted(input_list)
    
    if len(input_list) % 2 == 0:
        upper_val = input_sorted[len(input_sorted)//2]
        lower_val = input_sorted[len(input_sorted)//2-1]
        median = (upper_val + lower_val)/2
    else:
        median = input_sorted[len(input_sorted)//2-1]
    return median

# We define a custom variance function, making use of the mean function
def custom_variance(input_list: list) -> float:
    # Use the mean function to compute the mean
    mean = custom_mean(input_list)
    
    # Instantiate a temporary list
    variance_temp = []

    # Append the squared differences to the list
    for c_i in input_list:
        variance_temp.append((c_i-mean)**2)

    # Computing variance as the mean of the squared differences
    # Here we could also use the custom_mean() function if we want
    variance = 1/len(input_list) * sum(variance_temp)

    return variance

# We define the standard deviation of a list by first computing the variance
# then returning its square root
def custom_std(input_list: list) -> float:
    variance = custom_variance(input_list)
    return variance**(1/2)

# With all the functions defined, we can group the operations like this:
mean = custom_mean(c)
median = custom_median(c)
variance = custom_variance(c)
std = custom_std(c)

# Now we print all the values rounded to 2 decimals, which we can do inside
# the string
print(f"mean value: {round(mean, 2)}")
print(f"median value: {round(median, 2)}")
print(f"variance: {round(variance, 2)}")
print(f"standard deviation: {round(std, 2)}")
