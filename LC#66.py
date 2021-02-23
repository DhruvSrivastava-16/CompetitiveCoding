#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:17:49 2021

@author: dhruv
"""

class Solution:
    def plusOne(self, l):
        c = 1;

        if l[-1] != 9:
            
            l[-1] = l[-1] + 1
            return 
        
        
        else:
            for i in range(len(l)-1,-1,-1):
                if l[i] == 9 and c==1:
                    l[i] = 0
                
                else:
                    l[i] = l[i] + 1
                    c = 0
                    return
                    
                
                
                    
                
            if l[0] == 0 and c==1:
                l.insert(0,1)
                    
            
            
            
        
        
s = Solution()
l = [9,9,9]
s.plusOne(l)
        