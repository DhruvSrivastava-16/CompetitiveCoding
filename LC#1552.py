#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:53:53 2021

@author: dhruv
"""

def ass_check(d,stalls,nc):
    count = 0;
    ans = [stalls[0]]
    count+=1
    prev = stalls[0]
    for i in range(1,len(stalls)):
        if count == nc:
            break;
        
        if stalls[i] - prev >= d:
            ans.append(stalls[i])
            prev = stalls[i]
            count+=1;
    
    
    if count == nc:
        return True
    
    else: 
        return False

class Solution:
    def maxDistance(self,stalls,num_cows):
        stalls.sort();
        low = stalls[0]
        high = stalls[-1]
        curr_ans = 0
        
        while(low<=high):
            mid = (low+high)//2
            
            check = ass_check(mid,stalls,num_cows)
            
            if check == True:
                low = mid+1;
                curr_ans = mid;
            
            else:
                high = mid - 1;
            
        return curr_ans
    
S = Solution();
print(S.maxDistance([79,74,57,22],4))
