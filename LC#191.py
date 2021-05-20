#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 00:13:58 2021

@author: dhruv
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        mask = 1
        count = 0
        for i in range(0,32):
            if(n & mask != 0):
                count+=1
            mask=mask<<1
        return count
            