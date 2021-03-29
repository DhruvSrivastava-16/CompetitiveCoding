#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:54:05 2021

@author: dhruv
"""

def Fib_Recursion(n):
    if(n==0):
        return 0
    
    if(n==1):
        return 1
    
    else:
        return Fib_Recursion(n-1)+Fib_Recursion(n-2)
    
    
    
    
n = int(input("Enter Value: "))
for i in range(0,n):
    print("Ith element ",i,":",Fib_Recursion(i))    