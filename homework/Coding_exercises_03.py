"""
# Homework Exercises Session 3
"""


"""
## Exercise 1: Arabic to Roman Numerals

Write a function arabic_to_roman(n: int) -> str that converts a positive integer
to a Roman numeral string.

For simplicity, do NOT use the subtraction rule:
  - 4  → "IIII"  (not "IV")
  - 9  → "VIIII" (not "IX")

Supported numerals: I=1, V=5, X=10, L=50, C=100, D=500, M=1000

Hint: store the numerals in a dictionary, then use a while loop starting
from the largest value and work your way down.

Test cases:
  - arabic_to_roman(17)   → "XVII"
  - arabic_to_roman(86)   → "LXXXVI"
  - arabic_to_roman(1555) → "MDLV"
"""

# Write your solution below:




"""
## Exercise 2: Scrabble Score

Write a function scrabble_score(word: str) -> int that computes the Scrabble
score for a given word. The function should work regardless of letter case.

Letter values:
  A, E, I, O, U, L, N, R, S, T  → 1
  D, G                          → 2
  B, C, M, P                    → 3
  F, H, V, W, Y                 → 4
  K                             → 5
  J, X                          → 8
  Q, Z                          → 10

Hint: store the letter values in a dictionary and iterate over the letters
in the (uppercased) word.

Test cases:
  - scrabble_score("quiz")    → 22  (Q=10, U=1, I=1, Z=10)
  - scrabble_score("cabbage") → 14
  - scrabble_score("PYTHON")  → 14
"""

# Write your solution below:




"""
## Exercise 3: Isogram

Write a function is_isogram(word: str) -> bool that checks whether a word
or phrase is an isogram — a text where each letter appears only once.

Rules:
  - Spaces and hyphens may appear multiple times and should be ignored
  - Letter case should be ignored

Hint: iterate through the letters and keep track of which ones you have
already seen, e.g. using a list or dictionary.

Test cases:
  - is_isogram("lumberjacks")  → True
  - is_isogram("background")   → True
  - is_isogram("six-year-old") → True
  - is_isogram("letter")       → False
  - is_isogram("balloon")      → False
"""

# Write your solution below:




"""
## Exercise 4: Anagram

Write a function is_anagram(word1: str, word2: str) -> bool that checks whether
two words are anagrams of each other. Letter case should be ignored.

An anagram uses exactly the same letters as another word, just rearranged.

Hint: two words are anagrams if their sorted letter lists are equal.

Test cases:
  - is_anagram("stone", "tones") → True
  - is_anagram("earth", "heart") → True
  - is_anagram("save", "vase")   → True
  - is_anagram("hello", "world") → False
"""

# Write your solution below:




"""
## Exercise 5: Decimal to Binary and Back

a) Write a function decimal_to_binary(n: int) -> str that converts a positive
   integer from decimal to binary without using Python's built-in bin() function.

   Hint: repeatedly divide n by 2 using integer division (//) and collect
   the remainders (%) — the remainders in reverse order form the binary number.

b) Write a function binary_to_decimal(b: str) -> int that converts a binary
   string back to a decimal integer without using int(b, 2).

   Hint: the rightmost digit has positional value 2^0, the next has 2^1, etc.

Test cases:
  - decimal_to_binary(26)         → "11010"
  - decimal_to_binary(73)         → "1001001"
  - decimal_to_binary(512)        → "1000000000"
  - binary_to_decimal("11010")    → 26
  - binary_to_decimal("1001001")  → 73
"""

# Write your solution below:




"""
## Exercise 6: Run-Length Encoding

Write a function run_length_encode(s: str) -> str that compresses a string
using run-length encoding: sequences of identical consecutive characters are
replaced by their count followed by the character.

A run of length 1 should be written without a count prefix.

Test cases:
  - run_length_encode("AAABBCCCCD")       → "3A2B4CD"
  - run_length_encode("ZZZZYYYYXXWWWWWW") → "4Z4Y2X6W"
  - run_length_encode("ABCD")             → "ABCD"
"""

# Write your solution below:
