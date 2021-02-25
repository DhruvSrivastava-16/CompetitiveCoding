#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:46:03 2021

@author: dhruv
"""

n = int(input("Enter Number: "))


high = n-1
low = 0
mid = 0
flag = -1;

while(low<=high):
    
    mid = (low+high)//2
    
    if(mid**2<n):
        low = mid+1;
    
    elif(mid**2>n):
        high = mid-1;
        
    else:
        flag = 1;
        break
    
    
    
if flag == 1:
    print("Perfect Square!")
    
else:
    print("Not a perfect square")
        
    
    