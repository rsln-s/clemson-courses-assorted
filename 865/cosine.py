from scipy import spatial
import math

x = [1.5,1.0]
y = [1.4, 1.6]
x = [i / math.sqrt((x[1])**2 + (x[0])**2) for i in x]
y = [i / math.sqrt((y[1])**2 + (y[0])**2) for i in y]
result = math.sqrt( (y[0] - x[0])**2 + (y[1] - x[1])**2 )
print("normalized :", ["%.3f" % i for i in x], "Distance from x", "%.3f" % result)
