"""
# Homework Exercises Session 2
"""


"""
## Exercise 1: Find the Largest Value

Write a program that finds the largest value in a list using a loop.
Do NOT use the built-in max() function — find the value yourself by iterating.

Hint: start by assuming the first element is the largest, then update as you go.

Test cases:
  - [1, 2, 3, 4, 5]        → 5
  - [5, 4, 3, 2, 1]        → 5
  - [7, 42, 17, 8, 9]      → 42
  - [3.2, 8.7, 1.4, 5.9]   → 8.7
"""

values = [7, 42, 17, 8, 9]

# Write your solution below:




"""
## Exercise 2: Determine Leap Year

Write a program that determines whether a given year is a leap year.

Rules (apply in order — more specific rules override general ones):
  - Divisible by 400 → leap year
  - Divisible by 100 → NOT a leap year
  - Divisible by 4   → leap year
  - Otherwise        → NOT a leap year

Test cases:
  - 1700, 1800, 1900, 2100 are NOT leap years
  - 2000, 2020, 2024, 2048 ARE leap years
"""

year = 2024

# Write your solution below:




"""
## Exercise 3: Raindrops

Write a program that builds and prints a raindrop string based on the factors
of a number. Apply all rules that match, in order:

  - If the number has 3 as a factor → add "Pling" to the result
  - If the number has 5 as a factor → add "Plang" to the result
  - If the number has 7 as a factor → add "Plong" to the result
  - If none of the above match      → print the number itself

Hint: use the modulo operator (%) to check divisibility, and build the
result string by concatenating pieces.

Test cases:
  - 28  → "Plong"           (7 is a factor)
  - 30  → "PlingPlang"      (3 and 5 are factors)
  - 34  → "34"              (no factors of 3, 5, or 7)
  - 105 → "PlingPlangPlong" (3, 5, and 7 are all factors)
"""

number = 105

# Write your solution below:




"""
## Exercise 4: Check if Sorted

Write a program that checks whether a list of numbers is sorted in ascending order.
Use a loop — do NOT use sorted() or any other built-in sorting function.

A list is considered sorted if each element is less than or equal to the next.

Test cases:
  - [1, 2, 3, 4, 5]     → sorted
  - [3, 7, 12, 18, 25]  → sorted
  - [0, 0, 2, 2, 9]     → sorted  (equal values are allowed)
  - [2, 6, 9, 8, 11]    → not sorted
  - [20, 15, 10, 5, 1]  → not sorted
"""

# Write your solution below:




"""
## Exercise 5: Print a Rectangle

Write a program that prints a filled rectangle border made of '#' characters.
Only the border should be '#'; the inside should be spaces.

Example for width=9, height=5:
  #########
  #       #
  #       #
  #       #
  #########

Hint: use a loop for each row, and inside that loop build a string character
by character using concatenation (+=), then print the completed row string.
"""

width = 9
height = 5

# Write your solution below:




"""
## Exercise 6: Count Rock Types

Given the list of rock samples below, count how many times each rock type appears.
Store the counts in a dictionary and print the results.

Expected output (order may vary):
  granite: 3
  limestone: 4
  sandstone: 2
  gneiss: 1

Hint: iterate through the list; for each rock, either add it to the dictionary
with a count of 1, or increment its existing count.
"""

rock_samples = [
    "granite", "limestone", "sandstone", "granite", "limestone",
    "limestone", "gneiss", "sandstone", "granite", "limestone"
]

# Write your solution below:





"""
## Bonus Exercise: Hamming Distance

The Hamming distance between two strings of equal length is the number of
positions where the characters differ.

Write a program that computes the Hamming distance between two DNA strands.

Test case:
  AACCTTGGAACCTTGG
  AATCTCGGAATCTTAG
    ^  ^    ^   ^
  Hamming distance = 4
"""

strand_a = "AACCTTGGAACCTTGG"
strand_b = "AATCTCGGAATCTTAG"

# Write your solution below:
