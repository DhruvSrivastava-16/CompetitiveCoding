# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:06:53 2021

@author: DHRUV
"""

import math

def minimumstepsto1(n,ans):
    if n<0:
        return math.inf
    
    if n==1:
        return 0
    
   
    if n%3==0:
        a = minimumstepsto1(n//3,ans) + 1
        
    else:
        a=99999
        
        
    if n%2==0:
        b = minimumstepsto1(n//2,ans)+1
        
    else:
        b = 9999
        
            
    c = minimumstepsto1(n-1,ans)+1
        
    ans[n] = min(a,b,c)
    
    return ans[n]
    
 
    
        
        

ans = [0]*100
n=int(input("Enter the value of n: "))
minimumstepsto1(n,ans)
print(ans[n])
