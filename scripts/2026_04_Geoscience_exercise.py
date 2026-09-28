"""
Geoscience exercise from 2026_04_NGI.py
"""
# Remember to add pangaeapy and mplstereonet to your uv environment
from pangaeapy import PanDataSet
import mplstereonet as mpls
import matplotlib.pyplot as plt

# Loading the data
data = PanDataSet(996181).data

# Inspect the type
print(type(data))
# returns a pandas.DataFrame

# Inspecting the data to see what's in there
print(data)

# Missing strike, only has the azimuth, so we need to calculate the strike
data["Strike"] = data["Azim"] - 90

# Preparing the ax
fig, ax = mpls.subplots()

# Iterating over the two different Facies
for facies, df in data.groupby("Facies"):
    
    # Had to debug this solution with chatgpt due to an error
    strikes = df["Strike"].to_numpy().copy()
    dips = df["Dip"].to_numpy().copy()

    # Poles can be plotted using the ax.pole() function
    ax.pole(strikes, dips, label=facies)

# Adding grid and legend to the figure
ax.grid()
ax.legend()

# Adding a title to the figure. I use suptitle because the ax title
# overlapped with the plot
fig.suptitle("BASE-5B core: bedding")
plt.show()
