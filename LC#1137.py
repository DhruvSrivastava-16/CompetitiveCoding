#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 02:39:01 2021

@author: dhruv
"""

# class Solution:
#     def tribonacci(self, n: int):
        
#         if n == 0: 
#             return 0
        
#         if n == 1 or n == 2:
#             return 1
        
#         return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

class Solution:
    def tribonacci(self, n: int):
        
        if n == 0: 
            return 0
        
11        if n == 1 or n == 2:
            return 1
        
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)


        

n = int(input("Enter nth number of tribo: "))
s = Solution()
tribo_ans = s.tribonacci(n)
        