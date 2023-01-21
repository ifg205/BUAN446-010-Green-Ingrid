# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:01:31 2023

@author: ifg205
"""

#Final 2022
import pandas as pd
import numpy as np
#import pickle

import matplotlib as mpl
import matplotlib.pyplot as plt

#read the file
my_data = pd.read_csv("Bananas.csv")   

my_data

my_data.columns

my_data.head()

my_data.describe()
# there are 48 entries and the statistics look reasonable. No outliers

my_data['DATE'].describe
#The date column is an object (a string)

#create a new column stored as a date
my_data['Date'] = pd.to_datetime(my_data['DATE'],
                              infer_datetime_format=True)

my_data.head()

# remove the date string
del my_data['DATE']

my_data
# we have one entry per month

#Generate plot
plt.style.use('fivethirtyeight')

plt.scatter(my_data['Date'], my_data['Bananas price per lb'],
            color='red',marker='^')
plt.xticks(fontsize=10)
plt.xlabel('Date')
plt.ylabel('Price per lb')
plt.title('Banana Prices in U.S.')
plt.show()



