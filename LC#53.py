#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 02:58:38 2021

@author: dhruv
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 02:20:36 2021

@author: dhruv
"""


#Kadane'sAlgorithm - Coding Blocks!!

class Solution:
    def maxSubArray(self, nums):
        maxsum = -100;
        currsum = -100;
        j = 0;
        f = 0;
        
    
        for i in range(0,len(nums)):
            
          
            currsum = currsum + nums[i] 
            
            if currsum > maxsum:
                maxsum = currsum;
            
            if currsum < 0:
                currsum  = 0;
                print(i,nums[i])
            
        
            
          
                
                
        
        return maxsum;
                
        
        
        
        
L = [-2,-1]
        
S = Solution();
ans = S.maxSubArray(L)


