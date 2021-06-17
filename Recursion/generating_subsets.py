# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:46:09 2021

@author: DHRUV
"""


def subsets(f,inn,i,curr):
    print(f,curr)
    x = len(inn)
    
    if x ==i:
        #print("final: ",curr,len(curr))
        return 
    
    subsets(1,inn,i+1,curr+inn[i])
    
    subsets(2,inn,i+1,curr)   

    

x = subsets(-1,"abc",0,"")
    
    
        