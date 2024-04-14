# plottask.py
# Program that uses matplotlib to make a histogram of a normal distribution and a plot of the function h(x)=x3.
# Author: Noemi Diaz



# TASK1
# Program that displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2.

import numpy as np
import matplotlib.pyplot as plt

# Set a seed value to reproduce the random data just once and alway be the same
np.random.seed(1)

# Generate 1000 randmo values from a normal distribution with mean 5 and standard desviation 2
data = np.random.normal(5, 2, 1000)

# Plot histogram
plt.hist(data, color= 'lightgreen')

#Adding details to histogram
plt.title ('Healthy life style Histogram')
plt.xlabel("sports activities")
plt.ylabel("frequency")
plt.legend()

# Show the plot
plt.show()



'''
# TASK2.
# Program that displays a a plot of the function  h(x)=x3 in the range 0 to 10

import numpy as np
import matplotlib.pyplot as plt

# Define the range 0 to 10 values
x = np.linspace(0, 10, 100)


# Define the range of x values
x = np.linspace(0, 10, 100)

# Calculate the values for y corresponding  for h(x) = x^3
h_x = x ** 3

# Plot the function
plt.plot(x, h_x, color='orange', linewidth=2)

# Adding details
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.title('The influence of professional experience in salary')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
'''


