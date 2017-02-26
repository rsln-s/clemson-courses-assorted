import sys
import math
import numpy as np # http://numpy.scipy.org/
import statistics as st
import matplotlib as mpl
## agg backend is used to create plot as a .png file
mpl.use('agg')
import matplotlib.pyplot as plt # http://matplotlib.sourceforge.net/

age = [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61]
fat = [9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]

fig = plt.figure()
	
hplot = fig.add_subplot(1,1,1)

hplot.hist(age, bins=[20, 30, 40, 50, 60, 70])

fig.savefig('hist.png', bbox_inches='tight')
