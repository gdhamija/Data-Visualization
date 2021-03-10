# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:31:10 2021

@author: Pa's
"""

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]

squares = [1,4,9,16,25]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# Set size of the tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()