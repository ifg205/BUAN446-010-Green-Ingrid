# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:21:44 2022

@author: ifg205
"""

# Exercise 2.12: Hourly Wage Calculator

      
# Initilize    
year = 0
hourly_wage = 10.00   # Original Hourly Range
good_increase = 0.03
bad_decrease = -0.03
review = 'None'

print('Year\t Review \t Wage')


while year < 7:
    print(f'{year:}        {review}       {hourly_wage:.2f}') 
    # for the next year, add or decrease wage
    year +=1
    if (year <= 5):                       #Employee has good reviews for five  years, then two bad reviews for two years
        review = 'Good'
    else:
        review = 'Poor'
    if (review == 'Good'):               #Change hourly rate based on review
        hourly_wage *= (1 + good_increase)
    else:
        hourly_wage *= (1 + bad_decrease)

# Print final year
print(f'{year:}        {review}       {hourly_wage:.2f}') 
