"""
# Homework Exercises Session 4

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
## Exercise 1: NumPy — Soil phase relationships

In geotechnics, the void ratio e describes how porous a soil is.
From the void ratio we can derive two other fundamental properties:

  Porosity:              n  = e / (1 + e)
  Saturated unit weight: γ_sat = (G_s + e) / (1 + e) * γ_w   [kN/m³]

where G_s = 2.68 (specific gravity of the soil particles)
and   γ_w = 9.81 kN/m³ (unit weight of water).

You measured the void ratio for five soil samples:

  e = [0.55, 0.65, 0.78, 0.90, 1.10]

Using NumPy arrays:

1. Convert the list to a NumPy array.
2. Compute the porosity n for each sample and print the result.
3. Compute the saturated unit weight γ_sat for each sample and print the result,
   rounded to 2 decimal places.
4. Print the mean and standard deviation of γ_sat, rounded to 2 decimal places.
5. Print the indices of samples where the porosity exceeds 0.45.
   Hint: apply a condition on the array, e.g. n > 0.45, and use np.where().
"""

e = [0.55, 0.65, 0.78, 0.90, 1.10]
G_s = 2.68
gamma_w = 9.81  # kN/m³

# Write your solution below:




"""
## Exercise 2: pandas — Exploring the CPT dataset

Load the CPT dataset used in the session and answer the questions below.
Print each answer with a short descriptive label.

The dataset contains cone penetration test (CPT) measurements. Relevant columns:
  "ID"        — unique sounding identifier
  "Depth (m)" — measurement depth
  "qc (MPa)"  — cone resistance
  "fs (kPa)"  — sleeve friction
  "SBT (-)"   — Robertson soil behaviour type (integer class 1–9)

1. Load the CSV file and print the first 5 rows using .head().
2. How many rows and columns does the dataset have?
   Hint: use the .shape attribute.
3. Print the minimum, maximum, and mean of the cone resistance qc (MPa).
   Round the mean to 2 decimal places.
4. How many measurements belong to each soil behaviour type (SBT)?
   Hint: use .value_counts() on the "SBT (-)" column.
5. Which sounding (ID) has the greatest maximum depth?
   Hint: group by "ID", take the max of "Depth (m)", then use .idxmax().
"""

data_path = "data/CPT_PremstallerGeotechnik_revised.csv"

# Write your solution below:




"""
## Exercise 3: matplotlib — Particle size distribution curve

A particle size distribution (grading) curve shows what fraction of a soil
sample passes through sieves of different opening sizes. It is always plotted
with the grain size on a logarithmic x-axis and % passing on a linear y-axis.

Two soil samples were tested in the lab:

  sieve_mm      = [0.063, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 31.5]
  passing_A_pct = [2, 7, 18, 38, 58, 76, 88, 95, 99, 100]   # well-graded sand
  passing_B_pct = [1, 2, 4, 72, 90, 95, 97, 99, 100, 100]   # poorly-graded sand

Create a single plot with both curves on it:

1. Plot both curves as lines. Use a different color and a descriptive label
   for each ("Sample A — well graded", "Sample B — poorly graded").
2. Set the x-axis to a logarithmic scale using ax.set_xscale("log").
3. Set axis labels: "Grain size (mm)" and "Cumulative passing (%)".
4. Set the y-axis limits from 0 to 100.
5. Add a grid (alpha=0.4) and a legend.
6. Give the plot the title "Particle size distribution".
7. Finish with plt.tight_layout() and plt.show().

Feel free to customize the plot further if you like, e.g. by changing line styles,
adding markers, or using a different color scheme.
"""

sieve_mm      = [0.063, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 31.5]
passing_A_pct = [2, 7, 18, 38, 58, 76, 88, 95, 99, 100]
passing_B_pct = [1, 2, 4, 72, 90, 95, 97, 99, 100, 100]

# Write your solution below:
