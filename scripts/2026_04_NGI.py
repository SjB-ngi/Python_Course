"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in March
2026 in 4x4 hour sessions.

This script contains the code that was written during the fourth session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
Modifications: Sjur Beyer, sjur.beyer@ngi.no
"""
# This part is just to make sure that all the folders we added exist
# We don't need to "add os to uv", because os is a standard package
import os
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists("plots"):
    os.makedirs("plots")

###########################
# session 4 on 1st of April 2026
###########################

# Recap of previous sessions

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
import numpy as np

number_list = [[2, 4, 6, 8],
               [3, 5, 7, 9]]

# We can turn the number list into an array by using np.array()
number_array = np.array(number_list)

# The array can be sliced by using indices. The colon symbol : retrieves all
# values for the axis which it is used.

print(number_array[1, 2])
# returns 7

print(number_array[1, :])

print(number_array[:, 0])

# the shape of the array can be queried and individual columns / rows accessed
print("array shape:", number_array.shape)

print("array size:", number_array.size)

# We can use the array to do numerical operations such as summing all elements
array_sum = number_array.sum()
print("array sum:", array_sum)

# We can also sum along specified axes. Using axis=0 sums the elements of all
# rows, whilst using axis=1 sums the elements of all columns
axis_sum = number_array.sum(axis=0)
print("axis sum:", axis_sum)

column_sum = number_array.sum(axis=1)
print("column sum:", column_sum)

# numpy has many functions for mathematical operations, these functions will
# work element-wise over arrays of matching shapes

# Say we want to sum the elements of two lists. Lets explore how this is done
# first with pure python using loops, then with numpy

# Pure python
list_a = [2, 4, 6, 8]
list_b = [3, 5, 7, 9]

list_sum = []

for a, b in zip(list_a, list_b):
    list_sum.append(a+b)

print("list sum:", list_sum)

# Numpy
array_a = np.array(list_a)
array_b = np.array(list_b)

array_sum = array_a + array_b
print("array sum:", array_sum)

# The numpy version is more readable, and understandable

# As a geotechnical example, we compute the normalized friction ratio Fr
# Fr is defined as fs / (qt - sig_0v) and is used in soil classification
fs = [0.5, 1, 1.5, 2, 2.5, 3, 3.5]
qt = [2, 4, 6, 8, 10, 12, 14]
sig_0v = [1, 2, 3, 4, 5, 6, 7]

# We convert the lists to numpy arrays to perform element-wise operations
array_fs = np.array(fs)
array_qt = np.array(qt)
array_sig_0v = np.array(sig_0v)

# The formula is applied element-wise using numpy array arithmetic
array_Fr = array_fs / (array_qt-array_sig_0v)

print("array Fr", array_Fr)

# Exercise 11

c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# We simply compute the statistics using the numpy functions
mean = np.mean(c)
median = np.median(c)
variance = np.var(c)
std = np.std(c)

# We print the results using f-strings and rounding the values to 2 decimals
print(f"mean value: {mean.round(2)}")
print(f"median value: {median.round(2)}")
print(f"variance: {variance.round(2)}")
print(f"standard deviation: {std.round(2)}")

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

data_path = "data/CPT_PremstallerGeotechnik_revised.csv"

# The norm is to import pandas using the abbreviation "pd"
import pandas as pd

# We read the CPT data into a pandas.DataFrame using the pd.read_csv() function

CPT_data = pd.read_csv(data_path)

print(CPT_data)

# Every dataframe has a header which we can get an overview of using .columns

print(CPT_data.columns)

print(type(CPT_data))

# pandas dataframes are indexed using a header key, which is similar to how
# dictionaries are indexed. The returned output when indexing a pandas dataframe
# is all of the values corresponding to the column belonging to the key

# Whole column with the key ID
print(CPT_data["ID"][0])

# pandas dataframes are structured like a single spreadsheet, so we can also
# access the value at a given row index using .loc
# Get a row
print(CPT_data.loc[0]["basin_valley"])

# We can also use logical indexing, where we specify a condition in square
# brackets after the dataframe indicating which values we want to retrieve

# Subset that satisfies the condition of depth > 50 m
print(CPT_data[CPT_data["Depth (m)"] > 50])

print(CPT_data[CPT_data["ID"] == 49])

# We can get basic statistics of dataframe using .describe()

CPT_statistics = CPT_data.describe()
print(CPT_statistics)

print(type(CPT_statistics))

# Since the terminal truncates the output due to the large amount of rows and
# columns, we can more easily inspect the result of .describe() by writing the
# results to an excel file using the .to_excel() function.

CPT_statistics.to_excel("data/CPT_statistics.xlsx")

print(CPT_statistics.loc["min"]["Fr (%)"])

# If we want to group the data in different subsets, we can use the .groupby()
# function. Here we specify a header key for which all unique elements will
# be grouped. The output of .groupby() is a collection of tuples with the value
# used for grouping and the subset where the column holds that value

print(CPT_data["test_type"].unique())
# returns all the unique items of a column

CPT_groups = CPT_data.groupby("test_type")

print(list(CPT_groups))

# These groups can be used to iterate over like this:
for groupname, data in CPT_data.groupby("test_type"):
    pass

# Or equivalently like this
for groupname, data in CPT_groups:
    pass


# Exercise 12

### Amount of datapoints in the dataset
# This is given simply by the length of the dataframe, which can be
# computed using len()
n_datapoints = len(CPT_data)
print(f"there are {n_datapoints} datapoints in the dataset")

### Amount of different soundings
# Here we can use the .unique() function to get all unique values
# of the ID column, and then use len() to get the amount of unique values
n_soundings = len(CPT_data["ID"].unique())
print(f"there are {n_soundings} soundings in the dataset")

### Different test types
# I will make an empty dictionary to hold the counts
test_counts = {}

# Now we group the data by test type using .groupby()
for test, data in CPT_data.groupby("test_type"):
    # For each group we get the amount of unique IDs
    # and save it in the dictionary using the test type as key
    test_counts[test] = len(data["ID"].unique())

print(f"there are {test_counts['CPT']} CPT, {test_counts['CPTu']} CPTu, {test_counts['SCPT']} SCPT, {test_counts['SCPTu']} in the dataset")

### Amount of basins
# We can use the .unique() function again to get all unique values
# of the basin_valley column, and then use len() to get the number of unique values
n_basins = len(CPT_data["basin_valley"].unique())

# Alternatively
n_basins = CPT_data["basin_valley"].nunique()

### Most tested basin
# Here we can use .groupby() again to group the data by basin
# and count the amount of unique IDs in each group
basin_counts = {}
for basin, data in CPT_data.groupby("basin_valley"):
    basin_counts[basin] = len(data["ID"].unique())

# Now we find the basin with the most tests
basin_most = None
basin_n_tests = None

# We loop through the dictionary items and keep replacing the most tested basin
# if we find a basin with more tests than the current most tested basin
for basin, count in basin_counts.items():
    if basin_n_tests is None:  # first iteration
        basin_most = basin
        basin_n_tests = count
    elif count > basin_n_tests:
        basin_most = basin
        basin_n_tests = count

### Deepest test
# We can find the deepest test by extracting the row with the maximum
# depth using .idxmax()
deepest = CPT_data.loc[CPT_data["Depth (m)"].idxmax()]

# We can see what that depth is by indexing the resulting series
deepest_depth = deepest["Depth (m)"]

# Similarly we can get the ID of the deepest test by indexing with "ID"
deepest_test = deepest["ID"]

# Printing
print(f"the tests come from {n_basins} different sedimentary basins with {basin_n_tests}, the most tests were made in {basin_most} with {deepest_depth} m, test {deepest_test} is the deepest test")


### plotting using matplotlib.pyplot
# matplotlib is a plotting library for python. It is very powerful and flexible
# and is often the preferred library for plotting in python.

# The norm is to import matplotlib.pyplot using the abbreviation "plt"
import matplotlib.pyplot as plt

# We can create a simple line plot using the .plot() function in pyplot

# First we select a subset of the data for a single sounding, here we select the
# sounding with ID 376. We can use logical indexing to retrieve only the rows
# belonging to that ID
ID = 376
cpt = CPT_data[CPT_data["ID"] == ID]

# The cpt variable is a DataFrame which is a subset of the original CPT_data DataFrame,
# containing only the rows where the "ID" column is equal to 376.

# We can now plot the cone resistance qc (MPa) against depth (m) using the .plot() function
plt.plot(cpt["qc (MPa)"], cpt["Depth (m)"], c="black")

# We have to invert the y axis to get the depth increasing downwards, which is the convention
plt.gca().invert_yaxis()

# We add some labels and a title to the plot using .xlabel(), .ylabel() and .title()
plt.xlabel("qc (MPa)")
plt.ylabel("Depth (m)")
plt.title(f"CPT ID: {ID}")


# Finally we call plt.show() to display the plot. This is necessary to tell matplotlib
# that we're ready to see the results
plt.show()

# We can use a loop to create and save a plot for each sounding automatically
# The preferred way to create more complex plots is to use plt.subplots()
# NOTE: sharey=True makes all subplots share the same y axis
# which means that inverting the y axis on one subplot inverts it for all subplots
for id in range(10):
    # Get the subset for the current ID
    cpt = CPT_data[CPT_data["ID"] == id]

    # We use ncols=2 to add two axes to our figure, we use sharey=True to
    # make the axes "share" the y axis
    fig, axes = plt.subplots(ncols=2, sharey=True)

    # We add to the first plot using the index 0 for the axes
    axes[0].plot(cpt["qc (MPa)"], cpt["Depth (m)"], c="black")

    # Since the y axis is shared, we only need to invert one of the axes
    axes[0].invert_yaxis()

    axes[0].set_xlabel("qc (MPa)")
    axes[0].set_ylabel("Depth (m)")

    # We add to the second plot using the index 1 for the axes
    axes[1].plot(cpt["fs (kPa)"], cpt["Depth (m)"], c="blue")
    axes[1].set_xlabel("fs (kPa)")

    fig.suptitle(f"CPT ID: {id}")
    fig.savefig(f"plots/CPT_id{id}.png")

    # After saving we "close" the fig to save memory
    plt.close(fig)


# Exercise 13
# For the first plot we need a subset of the data that belongs to the sounding
# with ID 0. We can solve this by using logical indexing
cpt_df = CPT_data.loc[CPT_data["ID"] == 0]  # retrieve the part of the
                                            # dataframe belonging to ID 0

# We now initialize an empty plot using the .subplots() function in pyplot.
# Here we specify that we want to have two columns (ncols=2) of the subplot which allows
# us to access the two subplots like below. The .subplots() function has two
# outputs, the first of which is the figure object, and the second is the subplot
# "axes", which we add the data to.
fig, axs = plt.subplots(ncols=2, figsize=(8, 4))     # figsize gives the size
                                                     # of the plot in inches in
                                                     # the form (width, height)

# Here we can "unpack" the axs list to get some variables
# to work with
ax0, ax1 = axs  # This works because axs has only two elements

# We can add the data to the plot by using the .scatter() function, setting
# The color to be steered by the SBT value, and we assign a label for use
# in the legend
ax0.scatter(cpt_df["Fr (%)"], cpt_df["Qtn (-)"], c=cpt_df["SBT (-)"], label="raw data")

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
avg_Fr = cpt_df["Fr (%)"].mean()
avg_Qtn = cpt_df["Qtn (-)"].mean()

# Then we can add the new point to the plot with it's label for the legend
# We can set the size of the point using the "s" keyword
ax0.scatter(avg_Fr, avg_Qtn, label="average", s=80)

# We call .legend() to add the legend to the plot
ax0.legend()

# Now we shall add a histogram to the right hand plot, ax1

# First we create subsets for the SBT indices we're interested in
cpt_data_SBT7 = CPT_data[CPT_data["SBT (-)"] == 7]
cpt_data_SBT3 = CPT_data[CPT_data["SBT (-)"] == 3]

# We use the .hist() method to plot histograms for Qtn, here we specify the alpha
# to add transparency, we set the edgecolor of the histogram bars to be black,
# we specify labels for the legend and set density to be True, which normalizes
# the area of the histogram to 1
ax1.hist(cpt_data_SBT7['Qtn (-)'], alpha=0.5, edgecolor='black', label='soil type 7', density=True)
ax1.hist(cpt_data_SBT3['Qtn (-)'], alpha=0.5, edgecolor='black', label='soil type 3', density=True)

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
