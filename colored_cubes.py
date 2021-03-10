# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:50:43 2021

@author: Pa's
"""

import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

#Set chart label and chart titles

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Numbers", fontsize=16)
plt.ylabel("Cubes", fontsize=16)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
            edgecolor= 'none',s= 35)

plt.show()