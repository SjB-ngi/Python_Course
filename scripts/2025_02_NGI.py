# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics (Pilot course)"
from the Norwegian Geotechnical Institute. The course is held in May 2025 in 4x4 hour sessions.

This script contains the code that was written during the second session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 2 on 7th of May 2025
###########################


### Boolean operators: or, and, not
# These are used to do operations on True/False data, i.e boolean data
True, False

# not is used to reverse a boolean value
print(not True)
# prints False

print(not False)
# prints True

# or is used to check if at least one of the two boolean values is True
print(True or False)
# prints True

print(False or False)
# prints False

print(True or True)
# prints True

# and is used to check if both boolean values are True
print(True and False)
# prints False

print(False and False)
# prints False

print(True and True)
# prints True


a = 20

# comparison operators: <, >, <=, >=, ==, !=
# These are used to compare two values, and return a boolean value
print(a < 10)  # less than
print(a > 5)  # greater than
print(a <= 20)  # less than or equal to
print(a >= 20)  # greater than or equal to
print(a == 20)  # equal to
print(a != 21)  # not equal to


### control structures: conditional statements: if, elif, else, match cases

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False


rock_type = "dolomite"

# The code in the indentation block below will only run if the condition is True
if rock_type == "sandstone":
    print("The rock is indeed sandstone")

# elif can be used for additional tests NB! only if the first if statement
# is false
elif rock_type == "siltstone":
    print("The rock is siltstone")
else:
    print("The rock type is not familiar")

# match-cases are a new alternative to check if a variables matches something (==)
match rock_type:
    case "sandstone":
        print("The rock is indeed sandstone")
    case "siltstone":
        print("The rock is siltstone")
    case _:
        print("The rock type is not familiar")


### control structures: loops: while loop, for loop
# loops are used to repeat parts of code

# while loop is a loop that runs until a condition is not True anymore

while a < 30:
    print("a is small")

    a = a + 1  # alternative: a += 1


# Exercise 5
fibonacci_numbers = []

a, b = 0, 1
while a < 100:
    fibonacci_numbers.append(a)
    a, b = b, a + b  # a and b are modified after a is appended to the list
                     # to check the condition for the next iteration

print(fibonacci_numbers)



# a while loop can be used to iterate over a list

# The following two lists have items such that the indices match
ucs_list_MPa = [76, 85, 92, 78, 80]
rock_list = ["sandstone", "limestone", "limestone", "sandstone", "limestone"]

# We create an empty list to store the results
ucs_list_kPa = []

# create the i variable to use for iterating over the indices of the lists
i = 0

while i < len(ucs_list_MPa):
    # We get the values from the lists at the index i
    rock = rock_list[i]
    ucs_MPa = ucs_list_MPa[i]

    # We do the unit conversion, and add it to our result list
    ucs_kPa = ucs_MPa * 1000
    ucs_list_kPa.append(ucs_kPa)

    # We let the user know what has happened
    print(f"The ucs value of the {rock} is {ucs_MPa} MPa, converting to {ucs_kPa} kPa")

    # IMPORTANT: we increment i so the loop does not continue forever
    i += 1

# a better solution is however to use a for loop which is always finite

print()  # Empty prints are to separate the output

# We create an empty list to store the results
ucs_list_kPa = []

# for i in range(len(...)): is a typical construction to get an index

for i in range(len(ucs_list_MPa)):

    # We get the values from the lists at the index i
    rock = rock_list[i]
    ucs_MPa = ucs_list_MPa[i]

    # We do the unit conversion, and add it to our result list
    ucs_kPa = ucs_MPa * 1000
    ucs_list_kPa.append(ucs_kPa)

    # We let the user know what has happened
    print(f"The ucs value of the {rock} is {ucs_MPa} MPa, converting to {ucs_kPa} kPa")

print()
# Instead of iterating through indices, we may also iterate through
# the list elements
for ucs in ucs_list_MPa:

    # Here we also check if the ucs value is larger than 80 MPa
    # and print it only if it is
    if ucs > 80:
        print(f"the ucs value is {ucs}")


print()
# The enumerate() function can be used to get both an element and the index
for i, ucs in enumerate(ucs_list_MPa):
    rock = rock_list[i]
    print(f"the ucs of the {rock} is {ucs} MPa")

# zip will match the elements of two lists together by their indices
# and return a list of tuples which we can iterate over
print()
for rock, ucs in zip(rock_list, ucs_list_MPa):
    print(f"the ucs of the {rock} is {ucs}")


# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop
print()
[print(f"the ucs of the {rock} is {ucs} MPa") for rock, ucs in zip(rock_list, ucs_list_MPa)]

# it is short but comes at the price of readability


# Exercise 6

multiples = []

for i in range(1000):
    a = i % 3
    b = i % 5
    if a == 0:
        multiples.append(i)
    elif b == 0:
        multiples.append(i)

print(sum(multiples))

# Alternative solution, using the or operator and a sum variable

# Instead of summing the list, we can just sum the numbers directly
multiple_sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        multiple_sum += i

print(multiple_sum)


# Exercise 7

rocks = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff', 'quartzite', 'kaolin', 'phonolite', 'gneiss', 'sand', 'diabase', 'black coal', 'slate', 'andesite', 'andesite', 'gypsum and anhydrite', 'greywacke', 'suevite']

# we iterate using enumerate to get an iterator, i, which we can use to calculate the year
for i, rock in enumerate(rocks):
    # for the first iteration, i = 0, so we add 2007 to get the year 2007
    # for the second iteration, i = 1, so we add 2008 to get the year 2008
    # and so on
    year = 2007 + i

    # we format the string to include the year and the rock name
    print(f"the rock of the year {year} was {rock}")

