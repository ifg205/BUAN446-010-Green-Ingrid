# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 09:44:38 2023

@author: ifg205
"""

#Exercise 3.6: Turing Test
#import string

input('What is your problem? ')

result = input ('Have you had this problem before?').lower()

if result == 'yes':
    print('Well, you have it again.')
elif result == 'no':
    print ('Well, you have it now.')
else:
    print ('Well, you can\'t fix stupid')    



""" BTW, this script wouldn't convince anyone """