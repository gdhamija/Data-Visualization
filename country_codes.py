# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:53:48 2021

@author: Pa's
"""

from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """ Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # If the country wasn't found, return None.
        return None
    
print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))

