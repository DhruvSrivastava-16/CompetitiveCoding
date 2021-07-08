# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:09:39 2021

@author: DHRUV
"""

import heapq as h

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        ans_rooms = 0
        
        h_int = []
        h.heapify(h_int)
        
    
    
intervals = [[0,30],[5,10],[15,20]]
s = Solution()
