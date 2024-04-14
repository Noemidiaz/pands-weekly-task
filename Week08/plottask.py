# plottask.py
# Program that uses matplotlib to make a histogram of a normal distribution and a plot of the function h(x)=x3.
# Author: Noemi Diaz



# Task1. Program that displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2.

import numpy as np
import matplotlib.pyplot as plt

# Set a seed value to reproduce the random data just once and alway be the same
np.random.seed(1)

# Generate 1000 randmo values from a normal distribution with mean 5 and standard desviation 2
data = np.random.normal(5, 2, 1000)

# Plot histogram
plt.hist(data, color= 'lightgreen')

#Adding detail to histogram (Legend, color)
plt.title ('Healthy life style Histogram')
plt.xlabel("sports activities")
plt.ylabel("frequency")
plt.legend()

# Show the plot
plt.show()



# Task2. Program that displays a plot of the function  h(x)=x3 in the range 0 to 10.

