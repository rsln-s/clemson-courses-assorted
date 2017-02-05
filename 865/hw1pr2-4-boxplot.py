## numpy is used for creating fake data
import numpy as np 
import matplotlib as mpl 
import statistics as st

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt 

age = [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61]
fat = [9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]

print("Age: mean", st.mean(age), "median: ", st.median(age), "stdev: ", st.stdev(age))
print("Fat: mean", st.mean(fat), "median: ", st.median(fat), "stdev: ", st.stdev(fat)) 

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the scatter plot
bp = ax.scatter(np.array(age), np.array(fat))


# Save the figure
fig.savefig('fig2.png', bbox_inches='tight')
