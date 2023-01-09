# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:42:16 2023

@author: ifg205
"""

#Exercise 5.15: Tuples representing invoices

# Use a tuple to store the purchase information
items_purchased = ((83, 'Electric sander', 7, 57.98), 
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77, 'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50))
                   
#print original tuple with extended price and sale total
"""total_sale = 0
print("Using Original Tuple ")

print("ID    Description                     Qty     Price     Ext Price")

for part_number, part_description, qty, price in items_purchased:
    extended_price = qty * price
    total_sale += extended_price
    print(f'{part_number:<5} {part_description:<30} {qty:>3}   {price:>8.2f}     {extended_price:>9.2f}')
print(f'{"Total Sale   ": >54} {total_sale:>10.2f}')"""

from operator import itemgetter

#Sorting by part description
print("\nsorted by description")
items_by_desc = sorted(items_purchased,key=itemgetter(1))
total_sale = 0

print("ID    Description                    Qty      Price ")
for part_number, part_description, qty, price in items_by_desc:
    print(f'{part_number:<5} {part_description:<30} {qty:>3}   {price:>8.2f}')


# Sorting by price
print("\nsorted by price")
items_by_price = sorted(items_purchased,key=itemgetter(3))

print("ID    Description                    Qty      Price ")
for part_number, part_description, qty, price in items_by_price:
    print(f'{part_number:<5} {part_description:<30} {qty:>3}   {price:>8.2f}')


#Sorting by sales quantity
print("\nsorted by sales ranking")

qty_and_description = [(qty, part_description) for part_number, part_description, qty, price in items_purchased]

items_by_sales_ranking = sorted(qty_and_description, key = itemgetter(0))                      

print("Qty   Description")
for qty, part_description in items_by_sales_ranking:
    print(f'{qty:>3}   {part_description:<30}   ')
    
    
print("\nsorted by sales revenue")

revenue_and_description = [(qty * price, part_description) for part_number, part_description, qty, price in items_purchased]

items_by_revenue = sorted(revenue_and_description, key = itemgetter(0))                      


print("  Sales$   Description")
for revenue, part_description in items_by_revenue:
    print(f'{revenue:>8.2f}   {part_description:<30}   ')    
 
    
print("\nsorted by sales revenue with revenue between $200 and $500")

print("  Sales$   Description")
for revenue, part_description in items_by_revenue:
    if revenue >= 200.00 and revenue <= 500.00:
        print(f'{revenue:>8.2f}   {part_description:<30}   ')    
        
print("\nTotal of all invoices")     
total_sale = 0

for part_number, part_description, qty, price in items_purchased:
    extended_price = qty * price
    total_sale += extended_price
    
print(f'{"Total Sale   "} {total_sale:>10.2f}')
        
 