#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 21:51:22 2021

@author: dhruv
"""

L = [2,3,4,5,1]


l = 0 ; 
h = len(L) - 1; 

while (l<h):
    mid = (l+h)//2;
    print(mid)
    mins = L[mid]
    
    if L[mid] > L[mid + 1]:
        mins = L[mid + 1]
        break;
        
    if L[mid - 1] > L[mid]:
        mins = L[mid]
        break;
    
    if (mins > L[l]):
        print("ye")
        h = mid - 1;
        
        
    if (mins < L[h]):
        l = mid + 1
    
print ("Ans:",mins)