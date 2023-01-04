# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:37:45 2022

@author: ifg205
"""

# exercise 2.8: table with number of bacteria

print('Hour\t Number of Bacteria')
for hour in range(0,16,5):
    bacteria = 200 * 2 ** hour
    print(f'{hour:>4} {bacteria:>22}')
