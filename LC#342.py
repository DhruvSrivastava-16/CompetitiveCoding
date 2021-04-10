#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 20:05:24 2021

@author: dhruv
"""

class Solution:
    def isPowerOfFour(self, n):
        
        if(n<=0):
            return False
        
        mask = 1
        pos=0
        
        for i in range(0,31):
            if (n & mask == 1):
                break
            
            n = n>>1
            pos+=1
        
        print(pos)

        if pos%2==0 and pos>0:
            return True
        
        else:
            return False
        
        

n = 16
s = Solution()
answer = s.isPowerOfFour(n)
print(answer)
        