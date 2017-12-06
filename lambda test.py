# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 08:55:06 2017

@author: 
"""

def make_inc (n):
    return lambda x: x + n

"""
According to documentation, when make_inc is assigned to f with 5,
make_inc is, at that point, "closed" 
"""
f = make_inc (5)

print (f(3))
print (f(6))

