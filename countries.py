# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:51:58 2021

@author: Pa's
"""

from pygal.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
    