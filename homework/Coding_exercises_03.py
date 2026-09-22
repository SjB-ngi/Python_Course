"""
# Homework Exercises Session 3
"""

"""
## The CPT investigation challenge

You are helping with the early screening of ground conditions for a new
transport link. Work through the exercises in order: first inspect small field
datasets with NumPy, then investigate a real public CPT archive with pandas.

The engineering interpretations in these exercises are deliberately simple.
They are for practising Python, not for design decisions.
"""


"""
## Exercise 1: Screen three boreholes with NumPy

The rows in `core_recovery` are five consecutive core runs. The columns are
boreholes BH-A, BH-B, and BH-C. Every value is core recovery in percent.

Use NumPy to:

1. Convert `core_recovery` from a list of lists to an array.
2. Print the shape of the array.
3. Print all five results for BH-B (the second column).
4. Print the results from the third core run (the third row).
5. Calculate the mean core recovery for each borehole. Think carefully about
   which axis to use.
6. Use `np.argmin()` and `borehole_names` to print the name of the borehole
   with the lowest mean recovery.
"""

import numpy as np

borehole_names = np.array(["BH-A", "BH-B", "BH-C"])
core_recovery = [
    [92, 88, 95],
    [85, 71, 90],
    [78, 64, 87],
    [96, 82, 94],
    [89, 76, 91],
]

# Write your solution below:




"""
## Exercise 2: Calculate a CPT friction ratio

A processed cone penetration test (CPT) dataset provides corrected cone
resistance `qt`, sleeve friction `fs`, and total vertical stress `sigma_v`.
The normalized friction ratio is:

    Fr = fs / (qt - sigma_v) * 100 %

The units must match before calculating: `qt` is given in MPa, while `fs` and
`sigma_v` are in kPa. Use 1 MPa = 1000 kPa.

Using NumPy array operations and no loop:

1. Convert `qt` to kPa and calculate Fr at every depth.
2. Print the Fr array rounded to two decimals.
3. Print the mean and standard deviation of Fr, rounded to two decimals.
4. Use `np.argmax()` to print the depth with the highest Fr.
"""

depth_m = np.array([1, 2, 3, 4, 5, 6])
qt_mpa = np.array([2.4, 3.1, 1.8, 1.4, 4.8, 7.2])
fs_kpa = np.array([22, 35, 48, 55, 60, 72])
sigma_v_kpa = np.array([18, 36, 54, 72, 90, 108])

# Write your solution below:




"""
## Exercise 3: Calculate rock strength from laboratory data

A rock laboratory has sent raw results from uniaxial compression tests. The
failure load alone is not a strength: a larger specimen can carry a larger load
simply because it has a larger cross-sectional area.

Create a pandas DataFrame called rock_tests from lab_records. Then:

1. Add an area_mm2 column using the specimen diameter:

       area = pi * diameter**2 / 4

2. Add a ucs_mpa column:

       UCS = failure_load_kN * 1000 / area_mm2

   The conversion works because 1 kN = 1000 N and 1 MPa = 1 N/mm2.

3. Print the sample ID, rock unit, area, and UCS columns.
4. Use .describe() to inspect the distribution of the calculated UCS values.

Round only when printing; keep the unrounded values in the DataFrame.
"""

import pandas as pd

lab_records = {
    "sample_id": [
        "GRA-01", "GRA-02", "GRA-03", "GRA-04", "GRA-05",
        "GNE-01", "GNE-02", "GNE-03", "GNE-04", "GNE-05",
        "SCH-01", "SCH-02", "SCH-03", "SCH-04", "SCH-05",
    ],
    "rock_unit": [
        "Granite", "Granite", "Granite", "Granite", "Granite",
        "Gneiss", "Gneiss", "Gneiss", "Gneiss", "Gneiss",
        "Schist", "Schist", "Schist", "Schist", "Schist",
    ],
    "depth_m": [
        12.5, 18.0, 24.5, 31.0, 37.5,
        15.0, 21.5, 28.0, 34.5, 41.0,
        10.0, 17.0, 23.5, 30.0, 36.5,
    ],
    "diameter_mm": [
        50, 50, 54, 50, 38,
        50, 54, 50, 50, 38,
        38, 50, 50, 54, 38,
    ],
    "length_mm": [
        125, 98, 135, 130, 95,
        120, 135, 85, 125, 95,
        90, 125, 140, 135, 80,
    ],
    "failure_load_kN": [
        360, 310, 510, 400, 190,
        300, 420, 250, 330, 135,
        90, 180, 210, 260, 75,
    ],
    "failure_mode": [
        "valid", "valid", "valid", "end break", "valid",
        "valid", "valid", "valid", "valid", "end break",
        "valid", "valid", "valid", "valid", "valid",
    ],
}

# Write your solution below:



"""
## Exercise 4: Apply the laboratory QA rules

For this exercise, the laboratory manager accepts a test only when:

  - its length-to-diameter ratio is from 2.0 to 3.0, including both limits; and
  - its failure_mode is "valid".

These are simplified teaching rules, not a testing standard.

1. Add a length_diameter_ratio column.
2. Add an accepted column containing True or False for every test.
3. Use .loc to create accepted_tests and rejected_tests DataFrames.
4. Print the ID, ratio, and failure mode for every rejected test.
5. Print the number of accepted and rejected tests.

Hint: combine pandas conditions with &. Put each condition in parentheses.
"""

# Write your solution below:



"""
## Exercise 5: Did quality control change the conclusion?

Use only accepted_tests to calculate the count, mean, minimum, and maximum UCS
for every rock unit.

The pattern below applies several summary functions to each group:

    dataframe.groupby("column")["value"].agg(["count", "mean", "min", "max"])

Then:

1. Round the summary table to one decimal place and print it.
2. Print the rock unit with the highest accepted mean UCS.
3. Calculate the overall mean UCS before QA and after QA.
4. Print both means and their difference.

This is a useful engineering habit: check whether rejected measurements would
have changed the headline result.
"""

# Write your solution below:



"""
## Exercise 6: Make a rock-strength QA plot

A failure load versus UCS scatter plot can show why specimen geometry matters.

1. Plot accepted_tests with:
   - failure_load_kN on the x-axis;
   - ucs_mpa on the y-axis;
   - point colour set by diameter_mm;
   - the "viridis" colour map.
2. On the same axes, plot rejected_tests as large red x markers.
3. Add a title, useful axis labels, and a legend.
4. Save the figure as rock_strength_qa.png.

Starter pattern for putting the second dataset on the existing axes:

    axis = accepted_tests.plot.scatter(...)
    rejected_tests.plot.scatter(..., ax=axis)

Optional challenge: annotate each rejected point with its sample ID.
"""

import matplotlib.pyplot as plt

# Write your solution below:



"""
Useful references:
  - NumPy beginner guide: https://numpy.org/doc/stable/user/absolute_beginners.html
  - pandas groupby: https://pandas.pydata.org/docs/user_guide/groupby.html
  - pandas plotting: https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html
"""
