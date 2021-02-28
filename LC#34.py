#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 04:59:25 2021

@author: dhruv
"""

class Solution:
    def searchRange(self, nums, target):
        l = 0;
        h = len(nums) - 1;
        ans = [-1,-1]
        low = -1
        high = -1
        a = []
        k = 0;
        mid_B = (l+h)//2;

        
        while(l<=h):
            mid = (l+h)//2;
            
            
            if(nums[mid] == target ):
                low = mid
    
                h = mid - 1;
                
            elif(nums[mid] > target):
                h = mid - 1;
                
            else:
                l = mid + 1;
                
        
        l = 0;
        h = len(nums) - 1;
        a = []
        k = 0;
        mid_B = (l+h)//2;

        
        while(l<=h):
            mid = (l+h)//2;
            
            
            if(nums[mid] == target ):
                high = mid
                l = mid + 1;
                
            elif(nums[mid] > target):
                h = mid - 1;
                
            else:
                l = mid + 1;
                
        
        return [low,high]
        
s = Solution()
answer = s.searchRange([1,2,5,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,12,15,20], 8)
        
            
                
                
            
            
            
        
        