"""
- For a range of dimensionalities draw 10^6 uniformly randomly distributed data points
- Compute the pairwise distances for all data points
- Find max and min distances between the points
- Compute the fig_fig_ratios of the range of distances with relation to the minimum distance : (d_max - d_min) / d_min
- Plot the results
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import pairwise_distances

plt.xkcd()

max_vals = []
min_vals = []
ratio = []

# For a range of dimensionalities draw 10^6 uniformly randomly distributed data points
for n in range(3, 1002,5):
    data_points = np.random.uniform(size=(10000, n)) # this should be 1000000 but neither my computer nor google colab could cope with it.

    p = np.array(pairwise_distances(data_points)).flatten()
    p = list(filter(lambda a: a != 0, p))

    max_p = max(p)
    min_p = min(p)

    max_vals.append((n, max_p))
    min_vals.append((n, min_p))
    ratio.append((n, (max_p-min_p)/min_p))

# make a dataframe out of the values
df_max = pd.DataFrame(max_vals)
df_min = pd.DataFrame(min_vals)
df_ratio = pd.DataFrame(ratio)

# two subplots, one above each other
fig, axarr = plt.subplots(2,1)

fig_max_min = axarr[0]
fig_ratio = axarr[1]

# hide the top and right axes
fig_max_min.spines["top"].set_visible(False)
fig_max_min.spines["right"].set_visible(False)
fig_ratio.spines["top"].set_visible(False)
fig_ratio.spines["right"].set_visible(False)

# put the x and y tick marks in the correct places
# fig_max_min.set_xticks([0,500,1000])
# # fig_max_min.set_yticks([0,1])
# fig_ratio.set_xticks([0,500,1000])
# fig_ratio.set_yticks([0,1])

# Add labels
fig_max_min.set_xlabel("dimension")
fig_ratio.set_xlabel("dimension")
fig_ratio.set_ylabel("ratio")

# add the data to the plot
fig_max_min.plot(df_max[0], df_max[1])
fig_max_min.plot(df_min[0], df_min[1])
fig_ratio.plot(df_ratio[0], df_ratio[1])



# make sure the bottom label isn't cut off
plt.tight_layout()

plt.savefig("distances.png")
