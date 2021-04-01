#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:54:38 2021

@author: dhruv
"""

#Each painter takes Unit time (1) to paint the board 
#Each painter can only paint contiguous blocks

class Solution: 
    
    def ifpossible(self,mid, R,P):
        
        curr_p = 0;
        painters_needed = 1;
        painted = 0
        
    #    print("Curr MAx:",mid)
        
        for i in R:
        #    print('Con:',i+curr_p)
            if i + curr_p <= mid:
              #  print("Painter Painting:",painters_needed )
                curr_p = curr_p + i
              #  print("Curr_p",curr_p," i is:",i,"\n")
                
            else:    
                painters_needed += 1
                curr_p = i;
        
 #       print("Painters Needed: ",painters_needed,"\n" )
        
        if painters_needed <= P:
            return True
        
        else: 
            return False
            
            
                
            
    
    def answer(self,P,N,Board_Arr):
        l = 0
        h = sum(Board_Arr)
        ans = 99999
        while(l<=h):
            mid = (l+h)//2
            
            check = self.ifpossible(mid, Board_Arr, P)
            
            if check: 
                
                h = mid - 1
                ans = min(ans,mid)
            
            else:
                l = mid + 1
                
        return ans;
        
        
        
s = Solution()
P = 3
N = 6
B_A= [10, 20, 60, 50, 30, 40 ]

x = s.answer(P,N,B_A)
print(x)
        