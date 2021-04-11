#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:01:13 2021

@author: dhruv
"""

class Solution:
    def subsets(self,l):
        ans = []
        mask_length = 1 << len(l)
        for i in range(0,2**(len(l))):
            temp_ans = []
            temp_bin = bin(i | mask_length)[3:] 
            print(temp_bin)
            temp_ans_str = ''
            k = 0
            for i in temp_bin:
                if i == '1':
                    temp_ans.append(l[k])
                    
                k+=1
            
            ans.append(temp_ans)
            
        return ans
                    
                    
                    