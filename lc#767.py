# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:02:06 2021

@author: DHRUV
"""


class Solution:
    def reorganizeString(self, s):
        freq = [0]*26
        for i in s:
            freq[ord(i) - ord('a')] += 1
        
        print(freq)

s = Solution()
st = "aab"
s.reorganizeString(st)