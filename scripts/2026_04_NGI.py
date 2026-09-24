"""
Script for the "Python basics for geoscience and geotechnics" course
from the Norwegian Geotechnical Institute. The course is held in September
2026 in 4x4 hour sessions.

This script contains the code that was written during the fourth session
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Modifications: Sjur Beyer, sjur.beyer@ngi.no
Author: Dr. Georg H. Erharter
"""

###########################
# session 4 on 24th of September 2026
###########################

# recap

### plotting using matplotlib.pyplot
# matplotlib is a plotting library for python. It is very powerful and flexible
# and is often the preferred library for plotting in python.
# The norm is to import matplotlib.pyplot using the abbreviation "plt"


# Get some data to plot from our local resource


# We can create a simple line plot using plt.plot()
# The first argument is the x values, the second argument is the y values


# We can invert the y axis to have depth increasing downwards
# here we must use the gca() method to get the current axes object
# and invert the y axis with .invert_yaxis()


# We can set the x and y labels using plt.xlabel() and plt.ylabel()


# We can set the title using plt.title()


# Finally we show the plot using plt.show()


# The preferred way to create more complex plots is to use
# plt.subplots() to create a figure and axes objects
# NOTE: sharey=True makes all subplots share the same y axis
# which means that inverting the y axis on one subplot
# inverts it for all subplots

# axs is a list of axes objects, one for each subplot

# We can plot on each axes object using the .plot() method

# We can set the x and y labels using the .set_xlabel() and
# .set_ylabel() methods

# invert y axis (for all subplots since sharey=True)

# Adding more parameters
# Here we use a scatter plot for fs just to show that we can use
# different plot types on different subplots. The s parameter
# specifies the size of the markers


# For the third subplot we use a line plot again for u2, if it exists


# We can add a shared title for the entire figure using .suptitle()
# NOTE: This is using the figure object, not the axes object


# Similarly we show the plot using plt.show()



# Exercise 13

# Recap of the course and additional info

### Some domain relevant resources:
# - mplstereonet:   https://github.com/joferkington/mplstereonet
# - lasio:          https://github.com/kinverarity1/lasio
# - pylops:         https://github.com/PyLops/pylops
# - segyio:         https://github.com/equinor/segyio
# - gempy:          https://github.com/gempy-project/gempy
#
# - groundhog:      https://github.com/snakesonabrain/groundhog
# - python-ags4:    https://github.com/asitha-sena/python-ags4

# Domain exercise:
# To be completed in a separate script

# Field Manager API
# If you're interested in using the python API for the NGI developed platform Field Manager
# please contact either me, or the field manager team
# https://www.fieldmanager.io/support
