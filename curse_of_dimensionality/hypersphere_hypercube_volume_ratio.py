"""
Script to calculate and then plot the difference between the volume of a hypercube and the volume of the hypersphere contained within it.
"""

import math
import matplotlib.pyplot as plt
import pandas as pd

# xkcdify the plot
plt.xkcd()

# create lists to contain the values
ratio_sphere_to_cube = []
dimension = []

for x in range(1, 21):
    dimension.append(x)

    volume_of_hsphere = (math.pow(math.pi, x/2) / math.gamma(x/2 + 1)) * math.pow(1, x)
    volume_of_hcube = math.pow(2, x)

    ratio = volume_of_hsphere/volume_of_hcube

    ratio_sphere_to_cube.append(ratio)

# create a DataFrame to hold the data
df = pd.DataFrame(ratio_sphere_to_cube, dimension)

fig = plt.figure()
ax = fig.gca()

# hide the top and right axes
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# put the x and y tick marks in the correct places
ax.set_xticks([0,10,20])
ax.set_yticks([0,0.5,1])

# Add labels
ax.set_xlabel("dimension")
ax.set_ylabel("ratio of hypersphere to hypercube")

# add the data to the plot
plt.plot(df)

# make sure the bottom label isn't cut off
plt.tight_layout()

# save the figure into the current folder.
fig.savefig("ratio.png")
