# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:18:45 2021

@author: Pa's
"""

import pygal

wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl','co','ec','gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
