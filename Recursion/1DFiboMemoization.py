# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:40:38 2021

@author: DHRUV
"""

cache = {}

def fib(n):
    
    if n == 0:
        cache[n] = 0
        return 0
    
    if n == 1 or n == 2:
        cache[n] = 1
        return 1
    print(cache)
    
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
     
    else:
        return cache[n]
        
     
    
    


