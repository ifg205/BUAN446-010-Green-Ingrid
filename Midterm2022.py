# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 12:00:00 2023

@author: ifg205
"""

"""Exchange Rates ($1 equals)
Currency	How Much $1 is Worth in Currency
British Pound	0.84
Euro	0.95
Canadian Dollar	1.36 
Create a program which:

Defines a function to convert a given amount in US dollars 
to these 3 currencies at the exchange rates listed above.

When run, asks the user to input how many dollars 
they want to convert, then calls the function you defined, 
using it to convert the amount requested, and then 
prints each of the converted amounts to the console, 
indicating the amounts and currencies.  """


BRITISH_POUND   ='British Pound'
EURO            ='Euro'
CANADIAN_DOLLAR ='Canadian Dollar'
  


def currency_conversion(currency_name, us_dollar_amount):
    
    if currency_name == BRITISH_POUND:
        conversion_rate = 0.84
    elif currency_name == EURO:
        conversion_rate = 0.95
    elif currency_name == CANADIAN_DOLLAR:
        conversion_rate= 1.36
    return(us_dollar_amount * conversion_rate)


str = input('Enter amount in US Dollars to covert: ')

if str.isnumeric():
    us_amount = int(str)
    
    print(f'{us_amount:.2f}', '$ US in', BRITISH_POUND, 'is', f'{currency_conversion(BRITISH_POUND, us_amount):.2f}' )
    print(f'{us_amount:.2f}', '$ US in', EURO, 'is', f'{currency_conversion(EURO, us_amount):.2f}' )
    print(f'{us_amount:.2f}', '$ US in', CANADIAN_DOLLAR, 'is', f'{currency_conversion(CANADIAN_DOLLAR, us_amount):.2f}' )

else:
    print('Invalid input (Numbers only)')