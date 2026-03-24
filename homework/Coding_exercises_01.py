"""
# Homework Exercises Session 1
"""


"""
## Exercise 1: Rock Strength Report

Given the variables below, do the following:

1. Print a sentence using .format() that reads:
   "The UCS of granite is 175 MPa."
2. Print the same sentence using an f-string.
3. Create and print a filename string that looks like:
   "granite_175MPa.jpg"
   (use any combination of string formatting or concatenation)
"""

rock_name = "granite"
ucs = 175
unit = "MPa"

# Write your solution below:
print("The UCS of {} is {} {}.".format(rock_name, ucs, unit))
print(f"The UCS of {rock_name} is {ucs} {unit}.")
print(f"{rock_name}_{ucs}{unit}.jpg")



"""
## Exercise 2: Depth Measurement Slicing

You have a list of depth measurements (in meters) from a borehole investigation.
Using list slicing only (no loops), retrieve and print:

1. The first measurement
2. The last measurement
3. The first three measurements
4. The measurements from index 2 to index 5 (inclusive)
5. Every second measurement starting from the first
   Hint: slicing accepts a step value — [start:stop:step]
6. The entire list in reverse order
   Hint: a step of -1 reverses the list

"""

depths = [1.0, 2.5, 3.8, 5.1, 6.4, 7.7, 9.0, 10.3, 11.6, 13.0]

# Write your solution below:
print(depths[0])
print(depths[-1])
print(depths[0:3])
print(depths[2:6])
print(depths[::2])
print(depths[::-1])


"""
## Exercise 3: Rock Property Dictionary

The dictionary below maps rock names to a list: [ucs_in_MPa, density_in_kg_per_m3].

Using rock_properties, do the following:

1. Print the UCS of "sandstone" using an f-string, e.g.:
   "The UCS of sandstone is 90 MPa."

2. Add a new rock type of your choice to the dictionary.

3. Update the UCS value of "limestone" to 95 MPa.

4. Print the total number of rock types using len().
"""

rock_properties = {
    "sandstone": [90, 2350],
    "limestone": [80, 2600],
    "granite":   [200, 2650],
    "gneiss":    [150, 2700],
}

# Write your solution below:
# 1
print(f"The UCS of sandstone is {rock_properties['sandstone'][0]} MPa.")
# 2
rock_properties["mudstone"] = [20, 2500]
print(rock_properties["mudstone"])
# 3
rock_properties["limestone"][0] = 95
print(rock_properties["limestone"][0])
# 4
print(len(rock_properties)) # print total number of keys



"""
## Exercise 4: Geotechnical Formula

A soil sample has the following properties:
  - Total weight:  W = 4.5 kN
  - Total volume:  V = 0.25 m³
  - Water content: w = 0.18  (dimensionless)
  - Specific gravity of solids: Gs = 2.7
  - Unit weight of water: γ_w = 9.81 kN/m³

Compute and print each of the following, rounded to 2 decimal places,
with its unit in an f-string:

  1. Unit weight:        γ   = W / V                  [kN/m³]
  2. Dry unit weight:   γ_d  = γ / (1 + w)            [kN/m³]
  3. Void ratio:         e   = (Gs * γ_w / γ_d) - 1   [-]

"""

W = 4.5      # kN
V = 0.25     # m³
w = 0.18
Gs = 2.7
gamma_w = 9.81  # kN/m³

# Write your solution below:
γ = W / V
γ_d = γ / (1 + w)

print(f"Unit weight: γ = {γ:.2f} [kN/m³]")
print(f"Dry unit weight: γ_d = {γ_d:.2f} [kN/m³]")
print(f"Void ratio: e = {(Gs * gamma_w / γ_d) - 1:.2f} [-]")