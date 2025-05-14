# -*- coding: utf-8 -*-
"""
Script for the "Python basics for geoscience and geotechnics"
from the Norwegian Geotechnical Institute. The course is held in May 2025 in 4x4 hour sessions.

This script contains the code that was written during the fourth session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 4 on 14th of May 2025
###########################

# Lets define the list c again to use it in the next examples
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]


### importing scripts + coding style

# There are multiple ways to import functions from another script
# NOTE: The script must be in the same folder as the script you're using

# multiple functions can be imported at once by separating them with a comma
from python_course_utility import custom_mean, custom_variance

mean = custom_mean(c)
variance = custom_variance(c)

print(mean, variance)

# We can also import all functions from a script using the asterisk, *
from python_course_utility import *

std = custom_std(c)

print(std)

# If we want to import all functions from a script, we can also import the
# script itself
import python_course_utility

median = python_course_utility.custom_median(c)

print(median)

# To make the code more readable, we can import the script with an abbreviated
# name. This is done by using the "as" keyword
import python_course_utility as pcu

std = pcu.custom_std(c)

print(std)


### modules, code environments, module documentation
# Modules consist of python code written by others in the python community.
# Using modules lets us do more with python without having to implement the
# Functionality ourselves.

# All modules, or code we make for others to use, should be thoroughly
# documented. When you're using any community module you can check the
# documentation to find out how the module works

# Code environments hold collections of modules you have installed. In this
# course we have been using Anaconda, which provides a nice overview of your
# environments in the Anaconda Navigator.

# numpy works based on arrays and is much faster than classical loops
# The norm is to import numpy using the short name "np"

import numpy as np

c = [[1, 2, 3, 1],
     [3, 3, 2, 1],
     [4, 6, 4, 1]]

# We can turn the number list into an array by using np.array()
c_array = np.array(c)

print(c)
print(c_array)

# The array can be sliced by using indices. The colon symbol : retrieves all
# values for the axis which it is used.
print(c_array[0, :])  # First row, all values
print(c_array[:, 3])  # All values, fourth column


# the shape of the array can be queried and individual columns / rows accessed
print(c_array[1, -1])  # the indices are [row, column], so this code retrieves
                       # the last value of the second row

# We can use the array to do numerical operations such as summing all elements
print("Sum", c_array.sum())

# We can also sum along specified axes. Using axis=0 sums the elements of all
# rows, whilst using axis=1 sums the elements of all columns
print("Sum of each column", c_array.sum(axis=0))

print("Sum of each row", c_array.sum(axis=1))


# numpy has many functions for mathematical opreations, these functions will
# work element-wise over arrays of matching shapes

list_a = [2, 4, 6, 8]
list_b = [3, 5, 7, 9]
array_a = np.array(list_a)
array_b = np.array([3, 5, 7, 9])  # You will commonly see that people define the array using a list
                                  # directly in the np.array() function, instead of defining the list
                                  # first and then converting it to an array. This is a matter of preference


# Say we want to sum the elements of two lists. Lets explore how this is done
# first with pure python using loops, then with numpy

# loop version
sum_list = []

for a_i, b_i in zip(list_a, list_b):
    sum_list.append(a_i+b_i)

print(sum_list)

# numpy version
sum_array = array_a + array_b
print(sum_array)

# Numerical operators in python (+, -, *, /, //, %) work element-wise on arrays
product_array = array_a * array_b
print(product_array)

# Exercise 11




# numpy functions are highly optimized and faster than pure python code
# this means that operations done on large amounts of data can be substantially
# quicker using numpy


### data handling with pandas, data visualization with matplotlib

# pandas lets us load data in certain standardized formats, such as comma separated
# values (.csv) and excel files (.xlsx). This data is loaded as the standard
# data type in pandas, the pandas.DataFrame
import pandas as pd

# We install the openly available PremstallerGeotechnik dataset, which contains
# CPT data from various sites in Austria and Germany.
# https://www.tugraz.at/en/institutes/ibg/research/computational-geotechnics-group/database


# We unzip the data into a folder called "data" in our working directory. This
# lets us specify an easy file path to the unzipped .csv file

data_path = "data/CPT_PremstallerGeotechnik_revised.csv"


# We read the CPT data into a pandas.DataFrame using the pd.read_csv() function

CPT_dataframe = pd.read_csv(data_path)

print(CPT_dataframe.head())

# Every dataframe has a header which we can get an overview of using .columns
print(CPT_dataframe.columns)

# pandas dataframes are indexed using a header key, which is similar to how
# dictionaries are indexed. The returned output when indexing a pandas dataframe
# is all of the values corresponding to the column belonging to the key

print(CPT_dataframe["qt (MPa)"])


# pandas dataframes are structured like a single spreadsheet, so we can also
# access the value at a given row index using .loc
print(CPT_dataframe.loc[0])

# We can also use logical indexing, where we specify a condition in square
# brackets after the dataframe indicating which values we want to retrieve
print(CPT_dataframe[CPT_dataframe["qt (MPa)"] > 40])


# We can get basic statistics of dataframe using .describe()
CPT_statistics = CPT_dataframe.describe()

# Since the terminal truncates the output due to the large amount of rows and
# columns, we can more easily inspect the result of .describe() by writing the
# results to an excel file using the .to_excel() function.
CPT_statistics.to_excel("data/CPT_statistics.xlsx")


# If we want to group the data in different subsets, we can use the .groupby()
# function. Here we specify a header key for which all unique elements will
# be grouped. The output of .groupby() is a collection of tuples with the value
# used for grouping and the subset where the column holds that value
print()

for SBT, data in CPT_dataframe.groupby("SBT (-)"):
    # more code
    print(f"The amount of datapoints of class {SBT} is {len(data)}")


# Unique counts
np.unique(CPT_dataframe["ID"], return_counts=True)

# Finding the row with the max fs value
fs_max = CPT_dataframe.loc[np.argmax(CPT_dataframe["fs (kPa)"])]


# Exercise 12

# The amount of rows in the dataframe can be computed using the len() function
n_datapoints = len(CPT_dataframe)
print(f"there are {n_datapoints} in the dataset")

# Since we know the IDs start from 0 and increase by increments of 1, we can
# find the total amount of tests in the dataset using the max function of the
# ID column of the dataframe
n_IDs = max(CPT_dataframe["ID"])+1

# Alternatively we can use the .unique() function to check how many unique IDs
# there are and compute the length of the returned output
n_IDs = len(CPT_dataframe["ID"].unique())
print(f"there are {n_IDs} soundings in the dataset")

# Lets now count the number of tests of different types in the dataset.

# We instantiate a dictionary to hold the test types and their corresponding
# counts
test_dict = {}

# We can use the .groupby() function to group the dataframe by the test type
# And see how many unique IDs there are in each group by using the .nunique() function
for test_type, data in CPT_dataframe.groupby("test_type"):
    unique_IDs = data["ID"].nunique()

    # We can now add the test type and the number of unique IDs to the dictionary
    # The test type is the key, and the number of unique IDs is the value
    test_dict[test_type] = unique_IDs

# We print the count of each test type to the console
print(f"there are {test_dict['CPT']} CPT, {test_dict['CPTu']} CPTu, {test_dict['SCPT']} SCPT, {test_dict['SCPTu']} SCPTu in the dataset")

# alternatively we can make this more generic by using the string join function
# to create a string with the test type and the number of unique IDs
print("there are " + ", ".join([f"{test_type} {unique_IDs}" for test_type, unique_IDs in test_dict.items()]) + " in the dataset")


# We can count the number of basins by taking the length of the unique values
# in the "basin_valley" column
n_basins = len(CPT_dataframe["basin_valley"].unique())

# We now want to find the basin that has the most tests in it. For this we
# instantiate two "empty" variables, one holds the deepest value, the other
# holds the name of the corresponding basin valley

max_tests_basin = 0     # instantiated to 0 so it will be immediately overwritten
                        # by the code below

max_tests_basin_name = ''

# We can now iterate through the dataframe grouped by the basin valleys
for basin_name, data in CPT_dataframe.groupby("basin_valley"):

    # We compute the amount of tests in the given valley by taking the length
    # of the unique IDs in the subset of the dataframe
    tests_basin = len(data["ID"].unique())

    # If this value is higher than what we had before, we overwrite the variables
    if tests_basin > max_tests_basin:
        max_tests_basin = tests_basin
        max_tests_basin_name = basin_name

# To find the deepest depth measured and the sounding it belongs to we can
# locate the index where the test value is the deepest by using .idxmax()
# This will return the row index
deepest_index = CPT_dataframe["Depth (m)"].idxmax()

# Then we index the row of the dataframe using .loc, on that subset we further
# index the depth and ID using the header keys
deepest_depth = CPT_dataframe.loc[deepest_index, "Depth (m)"]
deepest_test  = CPT_dataframe.loc[deepest_index, "ID"]

print(f"there are {n_basins} sedimentary basins with {max_tests_basin}, the most tests were made in {max_tests_basin_name} with {deepest_depth}, test {deepest_test} is the deepest test")


### plotting using matplotlib.pyplot
# matplotlib is a plotting library for python. It is very powerful and flexible
# and is often the preferred library for plotting in python.

import matplotlib.pyplot as plt  # the norm is to import matplolib.pyplot as "plt"

# Exercise 13

# For the first plot we need a subset of the data that belongs to the sounding
# with ID 0. We can solve this by using logical indexing
CPT_data = CPT_dataframe[CPT_dataframe["ID"] == 0]    # retrieve the part of the dataframe
                                                      # belonging to ID 0

# We now initialize an empty plot using the .subplots() function in pyplot.
# Here we specify that we want to have two columns (ncols=2) of the subplot which allows
# us to access the two subplots like below. The .subplots() function has two
# outputs, the first of which is the figure object, and the second is the subplot
# "axes", which we add the data to.
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))     # figsize gives the size
                                                            # of the plot in inches in
                                                            # the form (width, height)

# We can add the data to the plot by using the .scatter() function, setting
# The color to be steered by the SBT value, and we assign a label for use
# in the legend
ax0.scatter(CPT_data["Fr (%)"], CPT_data["Qtn (-)"], c=CPT_data["SBT (-)"], label="raw data")

# Similarly we can change the scale to log-scale by using the following functions
ax0.set_xscale("log")
ax0.set_yscale("log")

# For the axis limits, we can use the .set_xlim() and .set_ylim() functions
# which allow us to specify left, right, bottom and top limits of the plot
ax0.set_xlim(left=0.1, right=10)
ax0.set_ylim(bottom=1, top=1000)

# We assign a grid to the plot, alpha gives the grid some transparency
ax0.grid(alpha=0.5)

# We can set the x and y labels using .set_xlabel() and .set_ylabel() respectively
ax0.set_xlabel("Fr (%)")
ax0.set_ylabel("Qtn (-)")

# We compute the mean of the parameters using the dataframe .mean() function
avg_Fr = CPT_data["Fr (%)"].mean()
avg_Qtn = CPT_data["Qtn (-)"].mean()

# Then we can add the new point to the plot with it's label for the legend
# We can set the size of the point using the "s" keyword
ax0.scatter(avg_Fr, avg_Qtn, label="average", s=80)

# We call .legend() to add the legend to the plot
ax0.legend()


# Now we shall add a histogram to the right hand plot, ax1

# First we create subsets for the SBT indices we're interested in
cpt_dataframe_SBT7 = CPT_dataframe[CPT_dataframe["SBT (-)"] == 7]
cpt_dataframe_SBT3 = CPT_dataframe[CPT_dataframe["SBT (-)"] == 3]

# We use the .hist() method to plot histograms for Qtn, here we specify the alpha
# to add transparency, we set the edgecolor of the histogram bars to be black,
# we specify labels for the legend and set density to be True, which normalizes
# the area of the histogram to 1
ax1.hist(cpt_dataframe_SBT7['Qtn (-)'], alpha=0.5, edgecolor='black', label='soil type 7', density=True)
ax1.hist(cpt_dataframe_SBT3['Qtn (-)'], alpha=0.5, edgecolor='black', label='soil type 3', density=True)

# Now we can set the label for the x axis in the same way as before and activate
# the legend
ax1.set_xlabel('Qtn (-)')
ax1.legend()

# plt.tight_layout() is nice to fill empty gaps in the plot
plt.tight_layout()

# In the very end, we run plt.show() to tell pyplot that we're ready to see the
# results
plt.show()


# Field Manager API
# If you're interested in using the python API for the NGI developed platform Field Manager
# please contact either me, or the field manager team
# https://www.fieldmanager.io/support
