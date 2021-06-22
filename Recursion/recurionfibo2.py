# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:36:43 2021

@author: DHRUV
"""


def fibo(n):
    print("Currently Summing Number: ",n)
    if n in cache:
        return cache[n]
    
    if n == 0: 
        return 0;
        
    if n == 1 or n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)

#this can speeded up by memoization