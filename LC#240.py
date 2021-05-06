#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:00:49 2021

@author: dhruv
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:40:03 2021

@author: dhruv
"""


#this is for the case when we know that its definitely there and we have to just find the 
#position of the "find" element. 
class Solution:
    def searchMatrix(self, l, find):
        
        cri = 0
        crj = len(l[0]) - 1
        
        lim = len(l)
        
        while(cri < lim and crj > -1):
            
            if l[cri][crj] == find:
                return True
                
            elif l[cri][crj] > find:
                crj -= 1;
                
            else:
                cri += 1;
        
        return False;
        
       
l = [[1,4,8,10],[2,5,9,15],[6,16,18,20],[11,17,19,23]]
target = 99

        

S = Solution()
ans = S.searchMatrix(l, target)


        
        