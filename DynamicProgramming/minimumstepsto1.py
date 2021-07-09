# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:37:37 2021

@author: DHRUV
"""


#top down approach
import sys

def minSteps(n,min_steps):
    
    print(n)
    
    if n<1:
        return sys.maxsize
    
    if n == 1:
        return 0
    if n%3 != 0:
        t3 = sys.maxsize
    
    else:
        t3 = minSteps(n//3,min_steps)
        
    if n%2 != 0:
        t2 = sys.maxsize
    
    else:
        t2 = minSteps(n//2,min_steps)
    
    min_steps[n] = min(t3,t2,minSteps(n-1,min_steps)) + 1
    
    return min_steps[n]
        
    
    
    #return min()


n = int(input("Enter Value of n: "))
min_steps = [0] * (100)
print("Ans: ",minSteps(n,min_steps))

#NOTE!!:
#There is a bottom up, iterative approach which is easier to imagine and code.

