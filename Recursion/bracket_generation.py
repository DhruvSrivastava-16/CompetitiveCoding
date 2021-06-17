# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:40:16 2021
@author: DHRUV
"""

def bracket_generator(out,curr_idx,n,openn,close,l):
     
    #base case
    if curr_idx == 2*n:
       
       
       l.append(out)    
      # print(out)
       
       return
      
    #recursion
    if (openn<n):
        out= out + '('
        bracket_generator(out, curr_idx + 1, n, openn + 1, close,l)
        out = out[:-1]


    if(close<openn):
        out = out + ')'        
        bracket_generator(out, curr_idx + 1, n, openn , close + 1,l)
        out = out[:-1]
        
    
    return l


                              #Dhruv#
                            #Srivastava#        
n = 2