# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:26:12 2021

@author: DHRUV
"""


#Reversing a set 

def rev(s):
    if len(s) == 0:
        return 
    
    s[-1] = s[0]
    rev(s[1:])

s = ["h","e","l","l","o"]
 