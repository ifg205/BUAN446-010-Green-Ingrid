# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:37:46 2023

@author: ifg205
"""

#Exercise 4.9 - Degrees to radians
# rad = degrees * pi / 180

import math as m

print ('Convert degrees to radians')
input_str = input('Enter degrees (0 to 180): ')

if input_str.isnumeric():
    input_number = int(input_str)
    if input_number >= 0 and input_number <= 180:
        radian = input_number * m.pi /180
        print(input_number, 'in degrees equals', radian, 'in radians')
    else: 
        print('Invalid input')
else: 
    print('Invalid input')