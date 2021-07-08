# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:47:15 2021

@author: DHRUV
"""


a = []
for i in range(0,16):
    l = bin(i)[2:]
    
    if len(l) > 3:
        k = int(l)
    
        print(l)