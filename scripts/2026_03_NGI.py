"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in September
2026 in 4x4 hour sessions.

This script contains the code that was written during the third session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Modifications: Sjur Beyer, sjur.beyer@ngi.no
Author: Dr. Georg H. Erharter
"""

###########################
# session 3 on 22nd of September 2026
###########################

# Let's start using AI to help us in this lesson, here is a prompt you can use to start the conversation:

"""
I'm a complete beginner in Python. Explain things in simple, casual language, with no assumed
programming knowledge. Keep answers very concise; usually 2-5 short sentences. Use tiny examples
when helpful, explain unfamiliar words immediately, and give me one small next step at a time. Avoid
jargon and long explanations unless I ask for more detail.
"""

### importing scripts + coding style

# Let's use the list from last session to test our functions with
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# There are multiple ways to import functions from another script
# NOTE: The script must be in the same folder as the script you're using

# We can import functions directly
from python_course_utility import custom_mean

# This lets us use the function as if it was written in this script
print(custom_mean(c))

# Multiple functions can be imported at once by separating them with a comma
from python_course_utility import custom_mean, custom_median, custom_variance

# If we want to import all functions from a script, we can also import the
# script itself

import python_course_utility

print(python_course_utility.custom_mean(c))


# To make the code more readable, we can import the script with an abbreviated
# name. This is done by using the "as" keyword

import python_course_utility as pcu

print(pcu.custom_mean(c))


### modules, code environments, module documentation
# Modules consist of python code written by others in the python community.
# Using modules lets us do more with python without having to implement the
# Functionality ourselves.

# All modules, or code we make for others to use, should be thoroughly
# documented. When you're using any community module you can check the
# documentation to find out how the module works

# Code environments hold collections of modules you have installed.

# numpy works based on arrays and is much faster than classical loops
# The norm is to import numpy using the abbreviation "np"

# > uv add numpy

import numpy as np

# Let's create a 2D list (a list of lists)
number_list = [[2, 4, 6, 8],
               [3, 5, 7, 9]]

# We can turn the number list into an array by using np.array()
print(number_list)

number_array = np.array(number_list)
print(number_array)

# The array can be sliced by using indices. The colon symbol : retrieves all
# values for the axis which it is used.

print(number_list[0][0])

print(number_array[0, 1])

print(number_array[0, :])
print(number_array[:, 1])

# the shape of the array can be queried and individual columns / rows accessed

print(number_array.size) # total number of elements in the array

print(number_array.shape) # dimensions of the array (rows, columns)

# We can use the array to do numerical operations such as summing all elements

# We can also sum along specified axes. Using axis=0 sums the elements of all
# rows, whilst using axis=1 sums the elements of all columns
print(number_array.sum(axis=0))

print(number_array.sum(axis=1))

# numpy has many functions for mathematical opreations, these functions will
# work element-wise over arrays of matching shapes

# Say we want to sum the elements of two lists. Lets explore how this is done
# first with pure python using loops, then with numpy
list_a = [2, 4, 6, 8]
list_b = [3, 5, 7, 9]

# pure python version
sum_list = []
for a, b in zip(list_a, list_b):
    sum_list.append(a+b)

print(sum_list)

# numpy version
array_a = np.array(list_a)
array_b = np.array(list_b)
print(array_a + array_b)

# For the numpy version, we can simply add the arrays directly without using loops

# Exercise 10
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

print(f"mean value: {np.mean(c).round(2)}")
print(f"variance: {np.var(c).round(2)}")
print(f"standard deviation: {np.std(c).round(2)}")

# numpy functions are highly optimized and faster than pure python code
# this means that operations done on large amounts of data can be substantially
# quicker using numpy

# A typical use case for element-wise operations is calculating derived parameters
# in geotechnical engineering

fs = [0.5, 1, 1.5, 2, 2.5, 3, 3.5]  # kPa
qt = [2, 4, 6, 8, 10, 12, 14]       # kPa
sig_0v = [1, 2, 3, 4, 5, 6, 7]      # kPa

def calculate_Fr(fs_list, qt_list, sig_0v_list):
    Fr = []
    for f, q, s in zip(fs_list, qt_list, sig_0v_list):
        result = f/(q-s)
        Fr.append(result)
    return Fr

print(calculate_Fr(fs, qt, sig_0v))

# numpy

def np_calculate_Fr(fs_list, qt_list, sig_0v_list):
    fs_array = np.array(fs_list)
    qt_array = np.array(qt_list)
    sig_0v_array = np.array(sig_0v_list)

    result = fs_array/(qt_array-sig_0v_array)
    return result


### data handling with pandas and simple data visualization

# pandas lets us load data in certain standardized formats, such as comma separated
# values (.csv) and excel files (.xlsx). This data is loaded as the standard
# data type in pandas, the pandas.DataFrame
# The norm is to import pandas using the abbreviation "pd"

# > uv add pandas

import pandas as pd

pd.DataFrame() # The DataFrame is the primary data structure in pandas, similar to an Excel spreadsheet

# We install the openly available PremstallerGeotechnik dataset, which contains
# CPT data from various sites in Austria and Germany.
# https://www.tugraz.at/en/institutes/ibg/research/computational-geotechnics-group/database


# We unzip the data into a folder called "data" in our working directory. This
# lets us specify an easy file path to the unzipped .csv file

data_path = "./data/CPT_PremstallerGeotechnik_revised.csv"


# # if using the jupyter interactive terminal, you can use the relative path like this
# data_path = "../data/CPT_PremstallerGeotechnik_revised.csv"

# We read the CPT data into a pandas.DataFrame using the pd.read_csv() function

CPT_data = pd.read_csv(data_path)

# Every dataframe has a header which we can get an overview of using .columns
print(CPT_data.columns)

# pandas dataframes are indexed using a header key, which is similar to how
# dictionaries are indexed. The returned output when indexing a pandas dataframe
# is all of the values corresponding to the column belonging to the key
CPT_data["basin_valley"]

# We can further index by specifying the row number after the column key
CPT_data["basin_valley"][0]

# Using the .at accessor is another way to access a single value for a row/column label pair
CPT_data.at[0, "basin_valley"]

# pandas dataframes are structured like a single spreadsheet, so we can also
# access the value at a given row index using .loc or .iloc
# NOTE that this indexing has to be done using square brackets as above

CPT_data.iloc[0]  # first row
CPT_data.iloc[1]  # second row

# We can also use logical indexing, where we specify a condition in square
# brackets after the dataframe indicating which values we want to retrieve
CPT_data[CPT_data["Depth (m)"]>10]  # Fetches the data where the condition evaluates to True

# You may also have multiple conditions, but use the element wise boolean operators (and -> &, or -> |)
CPT_data[(CPT_data["Depth (m)"]>10)&(CPT_data["qc (MPa)"]<10)]

# We can get basic statistics of dataframe using .describe()
cpt_stats = CPT_data.describe()

# If we want to group the data in different subsets, we can use the .groupby()
# function. Here we specify a header key for which all unique elements will
# be grouped. The output of .groupby() is a collection of tuples with the value
# used for grouping and the subset where the column holds that value

groups = CPT_data.groupby("test_type")  
# returns a list of elements like this: [(group-key, data), ... ]

# We can iterate through the groups using a for loop
for group_key, data in CPT_data.groupby("test_type"):
    print(group_key)

# Dataframes use numpy under the hood for efficient numerical computations
type(CPT_data["ID"].values)
# returns: numpy.ndarray

# Exercise 12

n_datapoints = len(CPT_data)
n_soundings = len(CPT_data["ID"].unique())
n_basins = len(CPT_data.groupby("basin_valley")) # Alternate way using .groupby()

# For the deepest test we index the dataframe at the row
index_where_depth_is_max = CPT_data["Depth (m)"].idxmax()

# We can use this index to fetch the row we're interested in using .iloc
deepest_test = CPT_data.iloc[index_where_depth_is_max]

print(f"there are {n_datapoints} datapoints in the dataset")
print(f"there are {n_soundings} soundings in the dataset")
print(f"The tests come from {n_basins} different sedimentary basins")
print()
print(f"the deepest test is ID: {deepest_test['ID']} ({deepest_test['Depth (m)']})")

# Pandas plotting:

# > uv add matplotlib

import matplotlib.pyplot as plt

# Pandas has a built-in .plot() method for making quick plots from a DataFrame
# or a Series. By default, .plot() creates a line chart. We first select one
# sounding, because plotting all 2.5 million measurements at once is not useful.

# Select the sounding to plot based on its ID
plot_id_cpt = 849

# Filter the dataframe to get only the rows corresponding to the selected sounding ID
sounding = CPT_data[CPT_data["ID"] == plot_id_cpt]

# Invert the depth values so that the plot has depth increasing downwards
sounding["Depth (m)"] = -sounding["Depth (m)"]
sounding.plot(
    x="qc (MPa)",
    y="Depth (m)",
    title=f"CPT ID: {plot_id_cpt}",
    xlabel="$q_c$ (MPa)",
    c="green"
)

# We can show the plot using plt.show() which opens a window with the plot
plt.show()

# We can save the plot to a file using plt.savefig()
plt.savefig(f"plots/quick_plot_cpt_id_{plot_id_cpt}")


# We can use .plot.bar() to compare categories. Here, .value_counts() counts
# the measurement rows for each Oberhollenzer class.

sounding["Oberhollenzer_classes"].value_counts().plot.bar(
    title=f"CPT ID: {plot_id_cpt}, Oberhollenzer classes"
    )
plt.show()
