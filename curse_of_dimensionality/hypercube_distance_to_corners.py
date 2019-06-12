"""
Script to calculate and then plot the distance to the corner of a hypercube with sides 2r from the center.
"""

import math
import matplotlib.pyplot as plt
import pandas as pd

# xkcdify the plot
plt.xkcd()

# create lists to contain the values
dimension = []
distance_to_corner = []

for x in range(1001):
    dimension.append(x)
    distance_to_corner.append(math.sqrt(x))

# create a DataFrame to hold the data
df = pd.DataFrame(distance_to_corner, dimension)

fig = plt.figure()
ax = fig.gca()

# hide the top and right axes
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add labels
ax.set_xlabel("dimension")
ax.set_ylabel("distance to corner")

# add the data to the plot
plt.plot(df)

# make sure the bottom label isn't cut off
plt.tight_layout()

# save the figure into the current folder.
fig.savefig("corner.png")
