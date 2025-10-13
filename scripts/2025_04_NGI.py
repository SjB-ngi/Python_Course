"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in October
2025 in 4x4 hour sessions.

This script contains the code that was written during the fourth session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""

###########################
# session 4 on 15th of October 2025
###########################


### importing scripts + coding style

# There are multiple ways to import functions from another script
# NOTE: The script must be in the same folder as the script you're using

# multiple functions can be imported at once by separating them with a comma


# We can also import all functions from a script using the asterisk, *


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

# Code environments hold collections of modules you have installed. In this
# course we have been using Anaconda, which provides a nice overview of your
# environments in the Anaconda Navigator.

# numpy works based on arrays and is much faster than classical loops
# The norm is to import numpy using the short name "np"


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


# Exercise 11


# numpy functions are highly optimized and faster than pure python code
# this means that operations done on large amounts of data can be substantially
# quicker using numpy


### data handling with pandas, data visualization with matplotlib

# pandas lets us load data in certain standardized formats, such as comma separated
# values (.csv) and excel files (.xlsx). This data is loaded as the standard
# data type in pandas, the pandas.DataFrame


# We install the openly available PremstallerGeotechnik dataset, which contains
# CPT data from various sites in Austria and Germany.
# https://www.tugraz.at/en/institutes/ibg/research/computational-geotechnics-group/database


# We unzip the data into a folder called "data" in our working directory. This
# lets us specify an easy file path to the unzipped .csv file


# We read the CPT data into a pandas.DataFrame using the pd.read_csv() function


# Every dataframe has a header which we can get an overview of using .columns


# pandas dataframes are indexed using a header key, which is similar to how
# dictionaries are indexed. The returned output when indexing a pandas dataframe
# is all of the values corresponding to the column belonging to the key


# pandas dataframes are structured like a single spreadsheet, so we can also
# access the value at a given row index using .loc


# We can also use logical indexing, where we specify a condition in square
# brackets after the dataframe indicating which values we want to retrieve


# We can get basic statistics of dataframe using .describe()


# Since the terminal truncates the output due to the large amount of rows and
# columns, we can more easily inspect the result of .describe() by writing the
# results to an excel file using the .to_excel() function.



# If we want to group the data in different subsets, we can use the .groupby()
# function. Here we specify a header key for which all unique elements will
# be grouped. The output of .groupby() is a collection of tuples with the value
# used for grouping and the subset where the column holds that value


# Exercise 12


### plotting using matplotlib.pyplot
# matplotlib is a plotting library for python. It is very powerful and flexible
# and is often the preferred library for plotting in python.


# Exercise 13



# Field Manager API
# If you're interested in using the python API for the NGI developed platform Field Manager
# please contact either me, or the field manager team
# https://www.fieldmanager.io/support
