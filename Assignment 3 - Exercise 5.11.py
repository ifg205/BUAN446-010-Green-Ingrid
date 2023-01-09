# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:35:25 2023

@author: ifg205
"""

#Exercise 5.11: Encryption Key

""" Write a function tha accepts a string as input and isolates the different unique
letter ignoring punctuation, spaces and case sensitivity.  The function should check
if the encryption key contains all lettes of the alphabet.  If not, the missing letters
should be added to the key"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def create_encryption_key(encryption_string):   
    lower_case_string = encryption_string.lower()  #make it all lower case
    
    packed_string = ""
    for index in range(0,len(lower_case_string)):  #eliminate spaces and punctuation
        if lower_case_string[index]  in ALPHABET:
            packed_string += lower_case_string[index]
    
    no_dup_string = ""                              #remove any duplicate letters
    for index in range(0,len(packed_string)):
        if packed_string[index] not in no_dup_string:
            no_dup_string += packed_string[index]

    cypher_string = no_dup_string                   #add any missing letters 
    for index in range(0,len(ALPHABET)):            
        if ALPHABET[index] not in no_dup_string:
            cypher_string += ALPHABET[index]
 
    
    return(cypher_string)


#Prompt for string

input_string = input("Enter a phrase to create encrytion key:")

key = create_encryption_key(input_string)

print("Encryption key:",key)