"""
Script to calculate the proportion of a hypersphere occupied by its shell.

1 - (1 - delta/r)^n
"""
import math
import matplotlib.pyplot as plt
import pandas as pd

plt.xkcd()

DELTA = 0.1
RADIUS = 1
proportion = []

for n in range(1000):
    proportion.append(1 - math.pow((1 - DELTA / RADIUS), n))

df = pd.DataFrame(proportion)

fig = plt.figure()
ax = fig.gca()

# hide the top and right axes
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# put the x and y tick marks in the correct places
ax.set_xticks([0,500,1000])
ax.set_yticks([0,0.5,1])

# Add labels
ax.set_xlabel("dimension")
ax.set_ylabel("ratio of hypersphere taken up by it's shell")

# add the data to the plot
plt.plot(df)

# make sure the bottom label isn't cut off
plt.tight_layout()

# save the figure into the current folder.
fig.savefig("shell.png")
