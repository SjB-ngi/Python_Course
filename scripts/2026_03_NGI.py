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


# This lets us use the function directly

# Multiple functions can be imported at once by separating them with a comma


# If we want to import all functions from a script, we can also import the
# script itself


# To make the code more readable, we can import the script with an abbreviated
# name. This is done by using the "as" keyword


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

# Let's create a 2D list (a list of lists)
number_list = [[2, 4, 6, 8],
               [3, 5, 7, 9]]

# We can turn the number list into an array by using np.array()


# The array can be sliced by using indices. The colon symbol : retrieves all
# values for the axis which it is used.


# the shape of the array can be queried and individual columns / rows accessed


# We can use the array to do numerical operations such as summing all elements


# We can also sum along specified axes. Using axis=0 sums the elements of all
# rows, whilst using axis=1 sums the elements of all columns


# numpy has many functions for mathematical opreations, these functions will
# work element-wise over arrays of matching shapes

# Say we want to sum the elements of two lists. Lets explore how this is done
# first with pure python using loops, then with numpy
list_a = [2, 4, 6, 8]
list_b = [3, 5, 7, 9]


# pure python version

# numpy version

# We need to turn the lists into arrays


# element wise addition is done using the + operator

# Exercise 10
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]


# numpy functions are highly optimized and faster than pure python code
# this means that operations done on large amounts of data can be substantially
# quicker using numpy


### data handling with pandas and simple data visualization

# pandas lets us load data in certain standardized formats, such as comma separated
# values (.csv) and excel files (.xlsx). This data is loaded as the standard
# data type in pandas, the pandas.DataFrame
# The norm is to import pandas using the abbreviation "pd"

# > uv add pandas



# We install the openly available PremstallerGeotechnik dataset, which contains
# CPT data from various sites in Austria and Germany.
# https://www.tugraz.at/en/institutes/ibg/research/computational-geotechnics-group/database


# We unzip the data into a folder called "data" in our working directory. This
# lets us specify an easy file path to the unzipped .csv file

data_path = "./data/CPT_PremstallerGeotechnik_revised.csv"

# # if using the jupyter interactive terminal, you can use the relative path like this
# data_path = "../data/CPT_PremstallerGeotechnik_revised.csv"

# We read the CPT data into a pandas.DataFrame using the pd.read_csv() function


# Every dataframe has a header which we can get an overview of using .columns


# pandas dataframes are indexed using a header key, which is similar to how
# dictionaries are indexed. The returned output when indexing a pandas dataframe
# is all of the values corresponding to the column belonging to the key


# pandas dataframes are structured like a single spreadsheet, so we can also
# access the value at a given row index using .loc
# NOTE that this indexing has to be done using square brackets as above


# We can also use logical indexing, where we specify a condition in square
# brackets after the dataframe indicating which values we want to retrieve



# We can get basic statistics of dataframe using .describe()


# If we want to group the data in different subsets, we can use the .groupby()
# function. Here we specify a header key for which all unique elements will
# be grouped. The output of .groupby() is a collection of tuples with the value
# used for grouping and the subset where the column holds that value


# The output is a tuple where the first element is the ID value of the group
# and the second element is a dataframe containing only the rows where the ID

# We can iterate through the groups using a for loop


# Dataframes use numpy under the hood for efficient numerical computations


# Exercise 12


# Pandas plotting:

# > uv add matplotlib


# Pandas has a built-in .plot() method for making quick plots from a DataFrame
# or a Series. By default, .plot() creates a line chart. We first select one
# sounding, because plotting all 2.5 million measurements at once is not useful.


# We can use .plot.bar() when we want to compare categories. Here,
# .value_counts() counts the measurement rows for each sedimentary basin, and pandas
# uses the basin names as the labels on the x-axis.


# Exercise 13


