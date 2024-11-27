# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics (Pilot course)"
from the Norwegian Geotechnical Institute. The course is held in November to
December 2024 in 4x4 hour sessions.

This script contains the code that was written during the second session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 2 on 27th of November 2024
###########################

# Exercise 4
rock_list = ["gneiss", "marl", "limestone"]
rock_tuple = ("gneiss", "marl", "limestone")

print(rock_list[0:2])
print(rock_tuple[0:2])

rock_list.append("greenschist")
# rock_tuple.append("greenschist")  # raises an AttributeError

rock_list[1] = "dolomite"
#rock_tuple[1] = "dolomite"  # raises a TypeError


### control structures: conditional statements: if, elif, else, match cases,
### operators

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False

a = 20

# == ... equal to
print(a == 20)

# != ... not equal to
print(a != 20)

# > or < ... greater or smaller than
print(a < 5)
print(a > 5)

# >= or <= ... greater than or equal or smaller than or equal
print(a <= 21)
print(a >= 20)

# these operators can be used in logical statements
rock_type = "sandstone"

if rock_type == "gneiss":
    # if the condiditon above is false, the code indented underneath will be skipped 
    print("The rock is a gneiss")

# elif can be used for additional tests NB! only if the first if statement
# is false
elif rock_type == "sandstone":
    # if the condiditon above is true, the code indented underneath will execute
    print("The rock is a sandstone")
elif rock_type == "limestone":
    print("The rock is a limestone")
else:
    print("Unrecognized rock type")
    
print(1+1)

# match-cases are a new alternative to check if a variables matches something (==)
match rock_type:
    case "gneiss":
        print("The rock is a gneiss")
    case "sandstone":
        print("The rock is a sandstone")
    case "limestone":
        print("The rock is a limestone")

### control structures: loops: while loop, for loop
# loops are used to repeat parts of code

# while loop is a loop that runs until a condition is not True anymore

a = 1
while a <= 10:
    print("a is less than 10")
    # We have to increment a, if not the line will run forever
    a = a + 1


# Exercise 5

limit = 200

# We instantiate a list containing the number 0, the first number of the series
fib = [0]

# We instantiate the iterator starting at 1, the second number of the series
number = 1

# We set the condition which will stop the loop when the number is above our limit
while number < limit:
    fib.append(number)  # We add the number to the list first, as we
                        # need to check the next one before adding that

    number = sum(fib[-2:])  # could also write: fib[-2] + fib[-1]

print(fib)


# a while loop can be used to iterate over a finite list like this

ucs_list = [76, 85, 92, 78, 80]  # iterable
rock_list = ["sandstone", "limestone", "limestone", "sandstone", "limestone"]

i = 0

while i < len(ucs_list):
    print(f"UCS value is {ucs_list[i]}")
    i += 1 # incrementing the iterator


# # a better solution is however to use a for loop which is always finite

# for i in range(len(...)): is a typical construction to get an index

for i in range(len(ucs_list)):
    # With the index, i, we can get the corresponding values in the
    # rock list and ucs list
    print(f"UCS value of the {rock_list[i]} is {ucs_list[i]} MPa")

# Instead of iterating through indices, we may also iterate through
# the list elements
for ucs in ucs_list:
    print(f"UCS value is {ucs} MPa")

# The enumerate() function can be used to get both an element and the index

for i, ucs in enumerate(ucs_list):
    print(f"UCS value of the {rock_list[i]} is {ucs} MPa")


# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop. To compare:

    
for ucs in ucs_list:
    # Within the iteration we can add additional conditions
    if ucs > 80:
        print(f"UCS value is {ucs} MPa")


# ... vs. the shorter list comprehension
ucs_statements = [f"UCS value is {ucs} MPa" for ucs in ucs_list if ucs > 80]

# it is short but comes at the price of readability

### Boolean operators: or, and, not
# These are used to do operations on True/False data, i.e boolean data

type(True)
# returns: bool

# "or" is used to check if at least one of two conditions are true

True or False
# returns: True

False or False
# returns: False

# "and" is used to check if two conditions are both true

True and True
# returns: True

True and False
# returns: False

# "not" is used to invert the boolean statement

not True
# returns: False

not True and False
# returns: True


# Exercise 6

numbers = []

total = 0

for number in range(1, 1000):
    if (number % 3 == 0) or (number % 5 == 0):  # We check if either of the two
                                                # conditions are true
        total += number

print(total)

# alternative as list comprehension
print(sum([number for number in range(1, 1000) if (number % 3 == 0) or (number % 5 == 0)]))


# Exercise 7
rocks = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff', 'quartzite',
         'kaolin', 'phonolite', 'gneiss', 'sand', 'diabase', 'black coal',
         'slate', 'andesite', 'andesite', 'gypsum and anhydrite', 'greywacke',
         'suevite']

# alternative with enumerate()

for i, rock in enumerate(rocks):
    year = 2007 + i
    print(f"the rock of the year in {year} is {rock}")

# alternative with zip()

years = list(range(2007, 2007+len(rocks)))
             
for rock, year in zip(rocks, years):
    print(f"The rock of the year in {year} was {rock}")
