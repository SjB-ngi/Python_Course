"""
Session 2: Python Basics for Geoscience and Geotechnics (March 18, 2026)

This module contains educational exercises covering fundamental Python concepts
including list operations, string manipulation, loops, and iterations.

Topics Covered:
    - List operations: creation, appending, slicing, and copying
    - String operations: length calculation and formatting
    - Loop constructs: while loops, for loops, enumerate(), and zip()
    - List comprehensions: concise syntax for creating filtered/transformed lists
    - Iteration patterns: indexing, element iteration, and parallel iteration

Exercises:
    Exercise 3: List population with string lengths and sum calculations
    Exercise 4: Sequence manipulation (lists vs tuples) - demonstrating mutability
    Exercise 5: Fibonacci sequence generation using while loops with conditions
    Exercise 6: Multiple-based sum calculation below 1000 using iteration
    Exercise 7: Apply enumerate functionality (index + value) to identify rock celebraties

Key Concepts:
    - Mutable vs immutable sequences (lists vs tuples)
    - Boolean operators: and, or, not
    - Comparison operators: ==, !=, <, >, <=, >=
    - Control flow: conditional statements (if/elif/else)
    - Loop control: break, continue
    - String formatting: .format() method and f-strings
    - Iteration methods: enumerate() for index+value, zip() for parallel iteration
    - List comprehensions: compact syntax for list transformations

Author: Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no, Andreas-Nizar Granitzer, andreas.nizar.granitzer@ngi.no
Instructor: Andreas-Nizar Granitzer
"""

###########################
# session 2 on 18th of March 2026
###########################

# Review Exercise 3

# TODO:
# - create a new empty list
# - compute the number of characters of the strings 'marl', 'gneiss', 'limestone', 'eclogite'
# - append the numbers to the empty list in the above given order
# - print the list
# - compute the sum of the last three elements of the list
# - print the result as a string “the result is: XX” two times by using the .format() method and an f-string.
# OUTPUT:
# - [4, 6, 9, 8]
# - 'the result is: 23'
# - 'the result is: 23'

# create a new empty list
empty_list = []

# compute the number of characters of the strings 'marl', 'gneiss', 'limestone', 'eclogite'
var_marl = "marl"
var_gneiss = "gneiss"
var_limestone = "limestone"
var_eclogite = "eclogite"

print(len(var_marl), len(var_gneiss), len(var_limestone), len(var_eclogite))

# append the numbers to the empty list in the above given order
populated_list = empty_list.copy()      # generate and allocate space for a new var depending on an existing one
populated_list.append(len(var_marl))    # add #chars from string-type variable var_marl
populated_list.append(len(var_gneiss))
populated_list.append(len(var_limestone))
populated_list.append(len(var_eclogite))

# print the list
print(populated_list)

# compute the sum of the last three elements of the list
result = sum(populated_list[-3:])
result_alt = sum(populated_list[::2]) # ind_start:ind_end:step
print(result, result_alt)

# Exercise 4

# TODO:
# - create a list and a tuple with the following content:
#       - rock_list = ['gneiss', 'marl', 'limestone’] => mutable
#       - rock_tuple = ('gneiss', 'marl', 'limestone’) => immutable
# - print the first two items of both sequences
# - append 'greenschist' to them
# - exchange the second element of both sequences with 'dolomite'
# OUTPUT:
# - ['gneiss', 'marl']
# - ('gneiss', 'marl')

# define list / tuple variables
rock_list = ['gneiss', 'marl', "limestone"]
rock_tuple = ('gneiss', 'marl', 'limestone')

# print the first two items of both sequences
print(rock_list[0], rock_list[1])
print(rock_tuple[0], rock_tuple[1])

print(rock_list[0:2], rock_tuple[:2])
print(rock_list[:2], rock_tuple[:2])

# append 'greenschist' to them
rock_list.append("greenschist")
print(rock_list)

# rock_tuple.append("greenschist") # will not work since immutable variable

# exchange the second element of both sequences with 'dolomite'
rock_list[1] = "dolomite"
print(rock_list)

################### BREAK 1 - 13:00 ###################

### Boolean operators: or, and, not
# These are used to do operations on True/False data, i.e boolean data
print(type(True))

# "not" is used to reverse a boolean value
print(not True)

# "or" is used to check if at least one of the two boolean values is True
print(True or False)

# "and" is used to check if both boolean values are True
print(True and False)

# comparison operators: <, >, <=, >=, ==, !=
# These are used to compare two values, and return a boolean value

################### SWITCH to slides ###################

### control structures: conditional statements: if, elif, else, match cases
# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False

a = 20

# ==
print(a == 20)

# !=
print(a != 20)

# <, >
print(a < 30)   # True
print(a > 30)   # False

# <=, >=
print(a <= 20)  # True
print(a >= 20)  # True

# The code in the indentation block below will only run if the condition is True
# demonstrate if-elif-else control structure

rock_type = "weathered mudstone"

# if-elif-else control structure works as on coherent unit / control structure
if rock_type == "gneiss":                       # check condition 1 yields False
    print(f"The rock is a gneiss.")

# elif can be used for additional tests NB! only if the first if statement
# is false
elif (rock_type == "sandstone"                  # check condition 2 yields False
      and rock_type == "weathered mudstone"
      and rock_type == "mudstone"):
    print(f"The rock is a {rock_type}.")

else:                                           # executed since condition 1 == condition 2 = False
    print("We dont know this rocktype.")

# if-elif-else control structure works as on coherent unit / control structure
number = 10

if number > 10:
    print("Greater than 10.")
elif number > 5:
    print("Greater than 5")
elif number > 0:
    print("Greater than zero.")

# multiple if-control structures are sequentially executed
if number > 10:
    print("Greater than 10.")
if number > 5:
    print("Greater than 5")
if number > 0:
    print("Greater than zero.")

# match-cases are a new alternative to check if a variables matches something (==)
match rock_type:
    case "gneiss": # ==
        print("The rock is gneiss.")
    case "sandstone":
        print("The rock is sandstone.")
    case "limestone":
        print("The rock is limestone.")
    case "weathered mudstone":
        print("The rock is weathered mudstone.")

### control structures: loops: while loop, for loop
# loops are used to repeat parts of code

################### BREAK 2 - 14:30 ###################

# NOTE: while loop is a loop that runs until a condition is not True anymore
while True:         # while condition == True
    print("abc")    # execute code block

    if (1==1):
        print("This is true.")

    if(2==2):
        break       # terminate the while loop using break keyword


# Exercise 5

# TODO:
# - create and print a list of all Fibonacci numbers that are smaller
#   than 200 using a while loop

# OUTPUT:
# - [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

fib_list  = [0, 1] # while / if-else / break => list with fibonacci numbers > 200
# expected result: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

while (fib_list [-1] < 200):
    next_value = fib_list [-1] + fib_list [-2]  # recursive

    if next_value < 200:
        fib_list .append(next_value)
    else:
        break   # "escape route" to avoid endless while loop

# a while loop can be used to iterate over a list
# The following two lists have items such that the indices match
ucs_list = [76, 85, 92, 78, 80]
rock_list = ["sandstone", "limestone", "limestone", "sandstone", "limestone"]

# We create the idx variable to use for iterating over the indices of the lists
idx = 0

# solution 1: while-loop
while idx < len(ucs_list):
    print(f"UCS value is {ucs_list[idx]}.")
    idx += 1

# solution 2: a better solution is however to use a for loop which is always finite # 1
for ucs_val in ucs_list:
    print(f"UCS value is {ucs_val}.")

# solution 3: hard coding
print(f"UCS value is {ucs_list[0]}.")
print(f"UCS value is {ucs_list[1]}.")
print(f"UCS value is {ucs_list[2]}.")
print(f"UCS value is {ucs_list[3]}.")
print(f"UCS value is {ucs_list[4]}.")

# for i in range(len(...)): is a typical construction to get an index; range acts als iterator (!= list variable)
for i in range(len(ucs_list)):
    print(f"UCS value of the {rock_list[i]} is {ucs_list[i]}")

print(f"test: {range(len(ucs_list))}")
print(f"length of ucs list = {len(ucs_list)}")

# Instead of iterating through indices, we may also iterate through
# the list elements
ucs_list = [76, 85, 92, 78, 80]
rock_list = ["sandstone", "limestone", "limestone", "sandstone", "limestone", "mudstone"]

# The enumerate() function can be used to get both an element and the index
for i, ucs in enumerate(ucs_list):
    print(f"UCS value of the {rock_list[i]} is {ucs}")

# zip will match the elements of two lists together by their indices
# and return a list of tuples which we can iterate over
for ucs, rock in zip(ucs_list, rock_list):
    print(f"UCS value of the {rock} is {ucs}")

# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop
for ucs in ucs_list:
    if ucs > 80:
        print(f"UCS value is {ucs} MPa.")

# it is short but comes at the price of readability
ucs_statements = [f"UCS value is {ucs} MPa" for ucs in ucs_list]
print(ucs_statements)

################### BREAK 3 - 15:30 ###################

#  Exercise 6

# TODO:
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# OUTPUT:
# - 233168

total = 0

for number in range(1, 1000):
    if (number % 3 == 0) or (number % 5 == 0):  # We check if either of the two
                                                # conditions are true
        total += number

print(total)


#  Exercise 6

# TODO:
# - The society of German geoscientists (Berufsverband Deutscher Geowissenschaftler)
#   award one “rock of the year” since 2007.
# - Write a scalable loop that prints out all rocks of the year since 2007 in the
#   form “The rock of the year {year} is {rock}”.
# - rocks = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff', 'quartzite’,
#   'kaolin', 'phonolite', 'gneiss', 'sand', 'diabase', 'black coal', 'slate', 'andesite', 'andesite', 'gypsum and anhydrite', 'greywacke', 'suevite']

# OUTPUT:
# - the rock of the year 2007 was granite
# - the rock of the year 2008 was sandstone
# - the rock of the year 2009 was basalt
# - the rock of the year 2010 was limestone
# - the rock of the year 2011 was tuff
# - the rock of the year 2012 was quartzite
# - the rock of the year 2013 was kaolin

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