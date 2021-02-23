#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 03:40:04 2021

@author: dhruv
"""

class Solution:
    def nextPermutation(self, a):
        if len(a) == 0:
            return None;
        
        maxi = a[-1]
        
        for i in range(len(a)-1,-1,-1):
            if i == -1:
                return a.sort();
            
            elif a[i] < maxi:
                a[-1],a[i] = a[i],a[-1]

                break
                
                
            
            
            
            
        
        
S = Solution()

nums = [1,2]

ans = S.nextPermutation(nums);

print("Next Permutation is:",nums)