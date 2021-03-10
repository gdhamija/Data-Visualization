# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:47:11 2021

@author: Pa's
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:14:38 2021

@author: Pa's
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active
while True:
    #Make arandom walk, and plot the points.
    rw = RandomWalk(500000)
    rw.fill_walk()
    
    # Set the size of the plotting window.
    plt.figure(figsize=(10,6))
    
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values,linewidth=1)
    
    #Emphasize the first and last points.
    #plt.plot(0,0, c='green', edgecolors='none)
    #plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', 
                #edgecolors='none', s=100)
    
    #Remove the axes .
    plt.axes().get_xaxis().set_visible(True)
    plt.axes().get_yaxis().set_visible(True)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    