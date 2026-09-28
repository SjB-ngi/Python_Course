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

# Recap

### plotting using matplotlib.pyplot
# matplotlib is a plotting library for python. It is very powerful and flexible
# and is often the preferred library for plotting in python.
# The norm is to import matplotlib.pyplot using the abbreviation "plt"

from export_single_cpt import lazy_cpt_loader

# Get some data to plot from our local resource
CPT_ID = 0 # input("Please give the ID to the CPT you want to plot: ")
cpt = lazy_cpt_loader(CPT_ID)

# Let us import the plotting library matplotlib.pyplot using the 
# convention of using "plt" as the abbreviation for matplotlib.pyplot
import matplotlib.pyplot as plt


# We can create a simple line plot using plt.plot()
# The first argument is the x values, the second argument is the y values

plt.plot(cpt["qc (MPa)"], cpt["Depth (m)"])

# We can invert the y axis to have depth increasing downwards
# here we must use the gca() method to get the current axes object
# and invert the y axis with .invert_yaxis()
plt.gca().invert_yaxis()

# We can set the x and y labels using plt.xlabel() and plt.ylabel()
plt.xlabel("$q_c$ [MPa]")
plt.ylabel("depth [m]")

# We can set the title using plt.title()
plt.title(f"CPT ID: {CPT_ID}")

# Finally we show the plot using plt.show()
# plt.show()


# The preferred way to create more complex plots is to use
# plt.subplots() to create a figure and axes objects
# NOTE: sharey=True makes all subplots share the same y axis
# which means that inverting the y axis on one subplot
# inverts it for all subplots
fig, axs = plt.subplots(ncols=2, sharey=True)
print(axs)
# axs is a numpy array of axes objects, one for each subplot

# We can plot on each axes object using the .plot() method
axs[0].plot(cpt["qc (MPa)"], cpt["Depth (m)"])

# We can set the x and y labels using the .set_xlabel() and
# .set_ylabel() methods
axs[0].set_ylabel("Depth [m]")
axs[0].set_xlabel("$q_c$ [MPa]")

# invert y axis (for all subplots since sharey=True)
axs[0].invert_yaxis()

# Adding more parameters
# Here we use a scatter plot for fs just to show that we can use
# different plot types on different subplots. The s parameter
# specifies the size of the markers
axs[1].scatter(cpt["fs (kPa)"], cpt["Depth (m)"], s=6, c=cpt["ID"])
axs[1].set_xlabel("$f_s$ [kPa]")

# For the third subplot we use a line plot again for u2, if it exists
if not all(cpt["u2 (kPa)"].isna()) and len(axs)>2:
    axs[2].plot(cpt["u2 (kPa)"], cpt["Depth (m)"])

# We can add a shared title for the entire figure using .suptitle()
# NOTE: This is using the figure object, not the axes object
fig.suptitle(f"CPT ID: {CPT_ID}")

# Similarly we show the plot using plt.show()
plt.show()

# Exercise 13
CPT_ID = 1
cpt_data = lazy_cpt_loader(CPT_ID)

# Initialize the figure and axis
fig, ax = plt.subplots()

# Scatter plot of the data, colored by SBT, label for the legend is "raw data"
ax.scatter(cpt_data["Fr (%)"], cpt_data["Qtn (-)"], c=cpt_data["SBT (-)"], label="raw data")

# Setting the axis to log in both x and y
ax.loglog()

# Adding the labels (also with added LaTeX formatting)
ax.set_xlabel("$F_r$ [%]")
ax.set_ylabel("$Q_{tn}$ [-]")
ax.grid()

# Defining the axis limits
ax.set_xlim(0.1, 10)
ax.set_ylim(1, 1000)

# Calculating the mean of the columns I need
avg = cpt_data[["Fr (%)", "Qtn (-)"]].mean()

# Adding the extra mean point
ax.scatter(avg["Fr (%)"], avg["Qtn (-)"], label="average")

# Adding the legend, which pulls from the labels
ax.legend()

# Displaying the plot
plt.show()
fig.savefig("./plots/exercise_13_figure")

# Recap of plotting and additional info

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
