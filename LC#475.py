#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:40:59 2021

@author: dhruv
"""

class Solution:
    
    def ifposs(self,mid,h,ht):
        s1 = len(h)
        s2 = len(ht)
        ht_used =  1;
        f = True
        
        for i in range(0,s1):
            
            if f == True:
                
                f = False
                for j in ht:
                    if abs(h[i]-j) <= mid:
                        f = True
                        break
                   
            
            if f == False:
                return False
                    
                    
                
        return True 
        

        
        
    def findRadius(self, houses, ht):
        l = 0
        houses.sort()
        ht.sort()
        if ht[-1] > houses[-1]:
            ans = ht[-1]
        
        else:
            ans = houses[-1]
        h = 100000
        
        while(l<=h):
            mid = (l+h)//2
            
            check = self.ifposs(mid,houses,ht)

            
            if check:
                h = mid - 1
                ans = min(ans,mid)
                
            else: 
                l = mid + 1
            
            
        
        return ans
        
        
houses = [1]
heaters = [1,2,3,4]
S = Solution();
ans = S.findRadius(houses, heaters)
print(ans)        