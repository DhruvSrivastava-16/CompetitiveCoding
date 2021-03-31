#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 01:42:45 2021

@author: dhruv
"""

class solution:
    
    def poss_check(self,R,L,P,mid):
        
        count = 0;
            
        par_list = [0 for i in range(L)]
        i = 0;
        t_par = 0
        tl_par = 0
        
    
        for i in range(L):
            t = R[i]; 
            tl_par = 0
            total_time = 0
            k = 2
            while  total_time + t <= mid: 
                t_par +=1
                tl_par += 1
                total_time += t
                t = R[i]*k;
                k+=1
                    
    
        if(t_par>=P):
            return True
        
        else: 
            return False
                
                
    
    def monotonicsearch(self,R,L,P):
        R.sort()
        
        l = 0
        h = sum([i*R[-1] for i in range(1,2*P)])
        ans = 99999

        while(l<=h):
            mid = (l+h)//2
                    
            check = self.poss_check(R,L,P,mid)
                    
            if check == True: 
                h = mid - 1
                ans = min(ans,mid)
                        
            else: 
                l = mid + 1;
                
        return ans
                
    
        
        
L = 4
R = [1,2,3,4]
P = 10

S = solution()
ans = S.monotonicsearch(R, L, P)
print("Answer:",ans)
