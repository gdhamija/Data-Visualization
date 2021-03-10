# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:43:48 2021

@author: Pa's
"""

import pygal

wm = pygal.Worldmap()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')