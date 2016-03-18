# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 02:43:22 2016

@author: Lisa is Awesome
"""

def count_pairs (dna, pair):
    return dna.count(pair)    
       

deoxys= raw_input("enter dna strand")    
doduo= raw_input("enter a pair")

print count_pairs(deoxys, doduo)
