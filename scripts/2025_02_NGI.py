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
# session 2 on 8th of October 2025
###########################

# Review Exercise 3

# Exercise 4, see code suggestion in 2025_01_NGI.py

### Boolean operators: or, and, not
# These are used to do operations on True/False data, i.e boolean data

# Boolean values are written as capitalized words:
True, False

# The datatype is "bool"
print(type(True))
# returns <class 'bool'>

# We can turn other datatypes into boolean values by using the bool() function
# Non-zero numbers and non-empty strings are True, zero and empty strings are False
print(bool(""))
# returns False

print(bool("string"))
# returns True

print(bool(0))
# returns False

print(bool(1))
# returns True

print(bool(100))
# returns True


# "not" is used to reverse a boolean value
print(not True)
# returns False

# "or" is used to check if at least one of the two boolean values is True
print(True or False)
# returns True

# "and" is used to check if both boolean values are True

print(True and True)
# returns True

# comparison operators: <, >, <=, >=, ==, !=
# These are used to compare two values, and return a boolean value

a = 10

# Less than
print(a < 10)
# returns False

# Less than or equal to
print(a <= 10)
# returns True

# Greater than
print(a > 10)
# returns False

# Greater than or equal to
print(a >= 10)
# returns True

# Is equal to
print(a == 5)
# returns False

# Is not equal to
print(a != 5)
# returns True


### control structures: conditional statements: if, elif, else, match cases

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False

a = 20

# Only if the expression after if is True, the code in the indentation block
# will be executed
if a < 10:
    print("a is less than 10")

# Elif can be used for additional tests, only if the first if statement
# is False
elif a == 10:
    print("a is 10")

# Else is used if none of the previous if or elif statements were True
else:
    print("a is greater than 10")

# In the case where you have multiple conditions to check, you can use
# multiple elif statements

material = "sand"
assumed_bulk_unit_weight = None  # initialize variable to None which means
                                 # that it has no value yet

if material == "clay":
    assumed_bulk_unit_weight = 18  # kN/m3
elif material == "till":
    assumed_bulk_unit_weight = 22  # kN/m3
elif material == "sand":
    assumed_bulk_unit_weight = 20  # kN/m3
else:
    assumed_bulk_unit_weight = 19  # kN/m3


# match-cases are a new alternative to check if a variables matches something (==)

assumed_bulk_unit_weight = None

match material:
    case "clay":  # same as if
        assumed_bulk_unit_weight = 18  # kN/m3
    case "till":  # same as elif
        assumed_bulk_unit_weight = 22  # kN/m3
    case "sand":  # same as elif
        assumed_bulk_unit_weight = 20  # kN/m3
    case _:  # same as else
        assumed_bulk_unit_weight = 19  # kN/m3



### control structures: loops: while loop, for loop
# loops are used to repeat parts of code

# while loop is a loop that runs until a condition is not True anymore

# Let's initialize a variable to use in the while loop (iterator)
a = 1

# Each round, the condition after while keyword is checked, if it is True,
# the code in the indentation block is executed
while a < 10:
    print(a)
    a += 1  # we increase a by 1 each round, otherwise
            # the loop would run forever


# Exercise 5

# Let's create with a list of the first two Fibonacci numbers
fib_list = [0, 1]

# First, I'll calculate the sum of the last two numbers in the list
last_two_sum = sum(fib_list[-2:])

# Each round we check if the last two numbers sum is less than 200
# If it is, we append it to the list
while last_two_sum < 200:
    fib_list.append(last_two_sum)
    last_two_sum = sum(fib_list[-2:])  # We update the sum of the last two
                                       # numbers before the next round

# Finally we print the list
print(fib_list)


# A while loop can be used to iterate over a list

# The following two lists have items such that the indices match
rocks = ["granite", "limestone", "sandstone"]
ucs_values = [90, 80, 87]

# We create the i variable to use for iterating over the indices of the lists
i = 0

# We can use the length of the list to know when to stop
while i < len(rocks):

    # Here we index the list with i to get the current rock
    # to print
    rock = rocks[i]
    print(f"the rock is {rock}")

    # We increase i by 1 each round to move to the next index
    i += 1


# A better solution is however to use a for loop which is always finite.
# Here are a couple of different ways to use for loops

# for i in range(len(...)): is a typical construction to get an index
for i in range(len(rocks)):
    rock = rocks[i]
    print(f"the rock is {rock}")

# Instead of iterating through indices, we may also iterate through
# the list elements directly
for rock in rocks:
    print(f"the rock is {rock}")

# The enumerate() function can be used to get both an element and the index
for i, rock in enumerate(rocks):
    ucs = ucs_values[i]
    print(f"the rock is {rock}, and the ucs is {ucs}")

# zip will match the elements of two lists together by their indices
# and return a list of tuples which we can iterate over
for ucs, rock in zip(ucs_values, rocks):
    print(f"the rock is {rock}, and the ucs is {ucs}")

# a "list comprehension" is a 1 line for loop as an alternative to a normal
# for loop
[print(f"the rock is {rock}, and the ucs is {ucs}") for ucs, rock in zip(ucs_values, rocks)]

# it is short but comes at the price of readability

# Exercise 6

# We specify the maximum number to check
maxNum = 1000

# We create an empty list to store the factors
factors = []

# We loop through all numbers from 0 to maxNum-1
for number in range(maxNum):

    # We use the "or" boolean operator to combine two conditions
    # If either condition is True, we append the number to the list
    if (number % 3 == 0) or (number % 5 == 0):
        factors.append(number)

# Finally we print the sum of the factors list
print(sum(factors))

# Alternative solution:

# We can also do the summation directly in the loop without storing
# the factors in a list
factor_sum = 0
for number in range(maxNum):
    # We use the "not" boolean operator to invert the condition
    # which interprets the result of the modulo operation as boolean
    # (0 is False, non-zero is True)
    if not number % 3:
        # If the number is a multiple of 3, we add it to the sum
        factor_sum += number

    # Instead of using "or" we can use "elif" to avoid adding
    # multiples of 15 twice
    elif not number % 5:
        factor_sum += number

# Now we can just print the result
print(factor_sum)

# Exercise 7
